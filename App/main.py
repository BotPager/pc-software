from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
)
from PySide6.QtCore import (
         QRunnable,
         QThreadPool,
         QTimer,
         Slot,
        )
from PySide6.QtGui import QPixmap
from PySide6 import QtGui
from  rc_resources import *
from worker import Worker
from comms import *
import time
import numpy as np
from ui_PCUI import Ui_MainWindow
import teams
import subprocess
import meshtastic
import meshtastic.serial_interface
import ftclive_queueteams
from pubsub import pub
import os
ICON_RED_LED = ":/icons/led-red-on.png"
ICON_GREEN_LED = ":/icons/green-led-on.png"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load UI
        state = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #always load to inputting pagers
        self.ui.stackedWidget.setCurrentIndex(0)
        #load teams
        self.ui.Pager_conn_indicator.setFixedSize(20, 20)
        self.ui.Pager_conn_indicator.setScaledContents(True)
        self.ui.Teams_set_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
        self.ui.Teams_set_indicator.setFixedSize(20, 20)
        self.ui.Teams_set_indicator.setScaledContents(True)
        self.ui.Automatic_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
        self.ui.Automatic_indicator.setFixedSize(20, 20)
        self.ui.Automatic_indicator.setScaledContents(True)
         
                
        self.teams = teams.create_teams()
        self.teams = teams.load_teams_from_file(self.teams,"teams.txt")
        self.display_loaded()
        self.set_teams()
        self.init_intensity()
       
        # Init Radio Communication
        self.radio = MeshGateway()
        self.radio.connect()
        self.radio.connection_changed.connect(self.update_connection)
       
        self.ui.load_teams.clicked.connect(lambda: self.open_file_picker("team_numbers"))
        self.ui.load_pid.clicked.connect(lambda: self.open_file_picker("pid"))
        self.ui.select_teams_file.clicked.connect(lambda: self.open_file_picker("teams"))

        # Connect page switches
        self.ui.SwitchManual.clicked.connect(self.show_manual_page)
        self.ui.SwitchPager.clicked.connect(self.show_set_pagers_page)
        self.ui.SwitchAuto.clicked.connect(self.show_automatic_page)

        # connect to team loading button
        self.ui.pushButton_2.clicked.connect(self.collect_team_data)

        #connect to send message butotn
        self.ui.MessageTeam.clicked.connect(self.send_message_manual)
        self.ui.pushButton_3.clicked.connect(self.close)
        self.ui.Message_single.clicked.connect(self.send_message_single)

        #start the automatic mode polling function
        self.ui.pushButton.clicked.connect(self.start_polling_timer)
        self.ui.pushButton.clicked.connect(self.update_automatic)
    
    def init_intensity(self):
        self.ui.Intensity.addItems(["Low","High"]) #index 0 is 1 index 1 is high 
        self.ui.Intensity.setPlaceholderText("Intensity")
        self.ui.Intensity.setCurrentIndex(-1)



    #code for managing the indicators
    def update_connection(self,connection):
        if connection:
            self.ui.Pager_conn_indicator.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        else:
            self.ui.Pager_conn_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
    def update_automatic(self,state):
        state = not state
        if state:
            self.ui.Automatic_indicator.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        else:
            self.ui.Automatic_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
    
    #shutdown logic
    def closeEvent(self, event):
        #occurs based on window closure
        print("window closed ending program")
        if hasattr(self, 'radio'):
            self.radio.exit()
        event.accept()


    # Page switching functions
    def show_manual_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_set_pagers_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_automatic_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    # Team data collection

    def collect_team_data(self):
        #remove teams to makesure they dont duplicate
        for i in range(0, 16):
            team_widget = getattr(self.ui, f"TeamN{i}", None)
            pid_widget = getattr(self.ui, f"PID{i}", None)
            if team_widget.text().strip() == "" or pid_widget.text().strip() == "" or team_widget.text().strip() == "-" or pid_widget.text().strip() == "-":
                print(f"{i} contains invalid")
                continue
            else:
                team_name = team_widget.text().strip()
                pid = pid_widget.text().strip()
                self.teams[i].name = team_name
                self.teams[i].pid = pid
                
        teams.save_teams_to_file(self.teams)
        print(self.teams)
        self.set_teams()
   
    # After loading all valid teams
    def set_teams(self):
        self.ui.TeamA_box.clear()
        self.ui.TeamB_box.clear()
        self.ui.TeamC_box.clear()
        self.ui.TeamD_box.clear()
        self.ui.TeamF_box.clear()

        for team in self.teams:
            if (team.name == "" or team.name == "-") and (team.pid == "" or team.pid == "-"):
                continue
            else:
                self.ui.TeamA_box.addItem(team.name,team)
                self.ui.TeamB_box.addItem(team.name,team)
                self.ui.TeamC_box.addItem(team.name,team)
                self.ui.TeamD_box.addItem(team.name,team)
                self.ui.TeamF_box.addItem(team.name,team)
    #debug info probably for what teams are validly loaded
    #currently dead code
    def print_teams(self):
        if len(self.teams) != 0:
            print("Valid teams loaded:")
            for t in self.teams:
                print(t)
                self.save_teams()
        else:
            print("no valid teams")

   
    def display_loaded(self):
            # Use enumerate to get the index (i) and the object (team) at the same time
            for i, team in enumerate(self.teams):
                # 1. Prevent breakage if you have more teams than UI slots (0-16)
                if i > 16:
                    break
                #Assign widget
                team_widget = getattr(self.ui, f"TeamN{i}", None)
                pid_widget = getattr(self.ui, f"PID{i}", None)

                #i think this does if this exist set the text with the string from team.name
                if team_widget:
                    team_widget.setText(str(team.name))

                if pid_widget:
                    pid_widget.setText(str(team.pid))


    #file picker for teams.txt, pid.txt,team_numbers.txt
    def open_file_picker(self, file_type):
        print("file picker")
        file_filter = "Text Files (*.txt);;All Files (*)"
        caption = "Select Teams File" if file_type == "teams" else "Select PID File"
        # Open the native dialog
        file_path, _ = QFileDialog.getOpenFileName(self, caption, "", file_filter)
        self.status_bar.showMessage(f"opening file picker {file_type}",timeout=3000)
        if file_path:
            if file_type == "team_numbers":
                # load team numbers after selected via file
                print(f"Team number file selected: {file_path}")
                team_numbers = teams.load_team_number(file_path)
                for i in range(0,len(team_numbers)):
                    self.teams[i].name = team_numbers[i]
                print(f"Team numbers: {team_numbers}")
            
            elif file_type == "pid":
                # If you want to handle the pid file specifically
                print(f"PID file selected: {file_path}")
                print(f"PIDS:")
                pids = teams.load_pid(file_path)
                for i in range(0,len(pids)):
                    self.teams[i].pid = pids[i]
                    
                print(teams.load_pid(file_path))
            elif file_type == "teams":
                self.teams = teams.create_teams()
                print(f"team object file selected: {file_path}")
                team = teams.load_teams_from_file(self.teams,file_path)
                print (team)
                self.teams = team
            self.display_loaded()

    #message sending manual mode
    #get the object from the currently selected team number (read index of current selection)
        #team a right
        #team b left
    #automatic may just use result from api matched against the array teams?
    urgency = ["FFFFFF","00FFFF","0000FF"] #i hope this helps rather than defining it inside send_message_manual
    def send_message_manual(self):
        #get data from currently selected teams
        TeamAObject=(self.ui.TeamA_box.itemData(self.ui.TeamA_box.currentIndex()))
        TeamBObject=(self.ui.TeamB_box.itemData(self.ui.TeamB_box.currentIndex()))
        TeamCObject=(self.ui.TeamC_box.itemData(self.ui.TeamC_box.currentIndex()))
        TeamDObject=(self.ui.TeamD_box.itemData(self.ui.TeamD_box.currentIndex()))
        Intensity_val = self.ui.Intensity.currentIndex() #intensity value is based on the array index becuase idk how to get the text value and this works fine ish
        print(f"intensity value = {Intensity_val}\n")
        match Intensity_val:
            case 1: #high
                intensity = self.urgency[2]
            case 0: #low
                intensity = self.urgency[1]
            case _: #default
                intensity = self.urgency[0]
           # print(f"intensity match {urgency}\n")
        self.radio.send_message(TeamAObject.pid, TeamBObject.pid,TeamCObject.pid,TeamDObject.pid,intensity)

    #single message
    def send_message_single(self):
        TeamFObject=(self.ui.TeamF_box.itemData(self.ui.TeamF_box.currentIndex()))
        self.radio.send_message_single(TeamFObject.pid,self.urgency[0])


    #functions for automatic mode
    #Automatic Mode - Polling Functions to stay within rate limits and check for queue changes
    def start_polling_timer(self):
        self.poll_interval_ms = 30000  # 30 seconds
        self.last_queue_signature = None
        self.api_cooldown_until = 0
        self.poll_timer = QTimer(self)
        self.poll_timer.timeout.connect(self.poll_for_queue_changes)
        self.poll_timer.start(self.poll_interval_ms)
        self.poll_for_queue_changes()  # Initial call to populate immediately

    def poll_for_queue_changes(self):
        now = time.time()
        if now < self.api_cooldown_until:
            print("In cooldown, skipping API call")
            return
        queue_details = ftclive_queueteams.get_queue_match_details()
        if queue_details is None:
            self.api_cooldown_until = now + 60  # Back off for 60 seconds
            return
        queue_signature = self.generate_queue_signature(queue_details)
        if queue_signature != self.last_queue_signature:
            print("Queue changed, sending messages")
            self.last_queue_signature = queue_signature
            teams_in_match = self.extract_teams_from_queue(queue_details)
            #DEBUG
            print ("Teams in match:", teams_in_match)
            print ("teams_in_match types:", [type(x) for x in teams_in_match])
            for team in self.teams:
                print(f"  team.name={team.name!r}, type={type(team.name)}, pid={team.pid!r}, match={team.name in teams_in_match}")
            teams_in_match_pid = [team.pid for team in self.teams if team.name in teams_in_match]
            print("teams_in_match_pid:", teams_in_match_pid)
            self.radio.send_message(teams_in_match_pid[0], teams_in_match_pid[1], teams_in_match_pid[2], teams_in_match_pid[3])   

    def generate_queue_signature(self, queue_details):
        # Create a simple signature based on team names and match number
        match_number = queue_details["matchBrief"]["matchNumber"]
        red_team1 = queue_details["matchBrief"]["red"]["team1"]
        red_team2 = queue_details["matchBrief"]["red"]["team2"]
        blue_team1 = queue_details["matchBrief"]["blue"]["team1"]
        blue_team2 = queue_details["matchBrief"]["blue"]["team2"]
        signature = f"{match_number}:{red_team1},{red_team2}:{blue_team1},{blue_team2}"
        return signature
    
    def extract_teams_from_queue(self, queue_details):
        red_team1 = str(queue_details["matchBrief"]["red"]["team1"])
        red_team2 = str(queue_details["matchBrief"]["red"]["team2"])
        blue_team1 = str(queue_details["matchBrief"]["blue"]["team1"])
        blue_team2 = str(queue_details["matchBrief"]["blue"]["team2"])
        return [red_team1, red_team2, blue_team1, blue_team2]
        
# Run application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
