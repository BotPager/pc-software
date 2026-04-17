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
    current_team_index=0
    def __init__(self):
        super().__init__()
        # Load UI
        state = False
        state2 = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #always load to inputting pagers
        self.ui.stackedWidget.setCurrentIndex(0)

        #load teams
        self.teams = teams.create_teams()
        self.teams = teams.load_teams_from_file(self.teams,"teams.txt")
        self.display_loaded()
        self.set_teams() 
 
        #setup indicators
        self.ui.Pager_conn_indicator.setFixedSize(20, 20)
        self.ui.Pager_conn_indicator.setScaledContents(True)
        self.ui.Pager_conn_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
        self.ui.Teams_set_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
        self.ui.Teams_set_indicator.setFixedSize(20, 20)
        self.ui.Teams_set_indicator.setScaledContents(True)
        self.ui.Automatic_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
        self.ui.Automatic_indicator.setFixedSize(20, 20)
        self.ui.Automatic_indicator.setScaledContents(True)
        self.ui.Errorbox.setReadOnly(True)
        self.ui.Pairbutton.setReadOnly(True)

       
        # Init Radio Communication
        self.radio = MeshGateway()
        self.radio.connect()
        self.radio.connection_changed.connect(self.update_connection)
       #file picker
       # self.ui.load_teams.clicked.connect(lambda: self.open_file_picker("team_numbers"))
       # self.ui.load_pid.clicked.connect(lambda: self.open_file_picker("pid"))
        self.ui.select_teams_file.clicked.connect(lambda: self.open_file_picker("teams"))

        self.ui.clear_all.clicked.connect(self.delete_all)
        
        # Connect page switches
        self.ui.SwitchManual.clicked.connect(self.show_manual_page)
        self.ui.SwitchPager.clicked.connect(self.show_set_pagers_page)
        self.ui.SwitchAuto.clicked.connect(self.show_automatic_page)
        self.ui.SwitchPair.clicked.connect(self.show_pair_page)
        self.ui.Provision_button.clicked.connect(self.provision)

        # connect to team loading button
        self.ui.pushButton_2.clicked.connect(self.update_teams_ind)
        self.ui.pushButton_2.clicked.connect(self.collect_team_data)

        #connect to send message butotn
        self.ui.MessageTeam.clicked.connect(self.send_message_manual)
        self.ui.pushButton_3.clicked.connect(self.close)
        self.ui.Message_single.clicked.connect(self.send_message_single)

        #start the automatic mode polling function
        self.ui.pushButton.setCheckable(True)
        self.ui.pushButton.clicked.connect(self.toggle_automatic_mode)

        self.poll_interval_ms = 30000  # 15 seconds (change to 30 for actual match time)
        self.last_queue_signature = None
        self.api_cooldown_until = 0
        self.poll_timer = QTimer(self)
        self.poll_timer.timeout.connect(self.poll_for_queue_changes)
    
    def delete_all(self):
        self.teams = teams.create_teams()
        self.display_loaded()
        self.set_teams() 
        return
    #code for managing the indicators
    def update_connection(self,connection):
        if connection:
            self.ui.Pager_conn_indicator.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        else:
            self.ui.Pager_conn_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
    def update_automatic(self,state):
        if state == True:
            self.ui.Automatic_indicator.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        else:
            self.ui.Automatic_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
    def update_teams_ind(self,state2):
        state2 = not state2
        if state2:
            self.ui.Teams_set_indicator.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
            QTimer.singleShot(3000, lambda: self.ui.Teams_set_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED)))
        else:
            self.ui.Teams_set_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))
              

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
    def show_pair_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def provision(self):
        self.ui.Pairbutton.clear()
        new_pid = self.radio.interface.getShortName()
        if new_pid:
            
            self.ui.Pairbutton.insertPlainText(f"Pager pid ={new_pid}\n")
            self.radio.provision()
        
            self.ui.Pairbutton.insertPlainText("Setting Channel and radio preset\n")
            # self.readio.provision()
            if new_pid:
                target_index = -1
                for i, team in enumerate(self.teams):
                    if not team.pid or team.pid == "Empty" or team.pid == "":
                        target_index = i
                        break
                if target_index == -1:
                    target_index = self.current_team_index
                    self.teams[i].pid = new_pid
                    # Move the pointer for the NEXT time we wrap around
                    self.current_team_index = (self.current_team_index + 1) % 15
                else:
                    self.teams[i].pid = new_pid
                    # If we found an empty slot, update the pointer to the slot AFTER it
                    self.current_team_index = (target_index + 1) % 15
                self.display_loaded()

            else:
                self.ui.Pairbutton.insertPlainText("error occured, no pid returned\n")
        else:
            self.ui.Pairbutton.insertPlainText("error device not connected")
        

    # Team data collection
    def collect_team_data(self):
        self.ui.Errorbox.clear()
        #remove teams to makesure they dont duplicate
        for i in range(0, 16):
            team_widget = getattr(self.ui, f"TeamN{i}", None)
            pid_widget = getattr(self.ui, f"PID{i}", None)
            if team_widget.text().strip() == "" or pid_widget.text().strip() == "" or team_widget.text().strip() == "-" or pid_widget.text().strip() == "-":
                self.ui.Errorbox.insertPlainText(f"{i} contains invalid")
                continue
            else:
                team_name = team_widget.text().strip()
                pid = pid_widget.text().strip()
                self.teams[i].name = team_name
                self.teams[i].pid = pid
                
        teams.save_teams_to_file(self.teams)
        self.ui.Errorbox.insertPlainText(f"{self.teams}\n")
        # print(self.teams)
        self.set_teams()
        # self.display_loaded()
   
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
        self.ui.Errorbox.insertPlainText(f"opening file picker {file_type}\n")   
        QTimer.singleShot(3000, lambda: self.ui.Errorbox.clear())
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
    urgency = ["FFFFFF","00FFFF","0000FF","FFFF00"] #i hope this helps rather than defining it inside send_message_manual
    def send_message_manual(self):
        #get data from currently selected teams

        field_num = (self.ui.Arena_select.currentText())
        print(str(field_num))
        TeamAObject=(self.ui.TeamA_box.itemData(self.ui.TeamA_box.currentIndex()))
        TeamBObject=(self.ui.TeamB_box.itemData(self.ui.TeamB_box.currentIndex()))
        TeamCObject=(self.ui.TeamC_box.itemData(self.ui.TeamC_box.currentIndex()))
        TeamDObject=(self.ui.TeamD_box.itemData(self.ui.TeamD_box.currentIndex()))
        Intensity_val = self.ui.Intensity.currentIndex() #intensity value is based on the array index becuase idk how to get the text value and this works fine ish
        print(f"intensity value = {Intensity_val}\n")
        match Intensity_val:
            case 2: #parts
                urgency = self.urgency[3]
                type = "parts"
            case 1: #high
                urgency = self.urgency[2]
                type = "high"
            case 0: #low
                urgency = self.urgency[1]
                type = "default"
            case _: #default
                urgency = self.urgency[0]
                type = "default"
        match type:
            case "default":
                messager = f"red team head to arena {field_num}\n"
                messageb = f"blue team head to arena {field_num}\n"        
                formatted =  f"{TeamAObject.pid}|{urgency}|{messager}{TeamBObject.pid}|{urgency}|{messager}{TeamCObject.pid}|{urgency}|{messageb}{TeamDObject.pid}|{urgency}|{messageb}"
            case "high":
                messager = f"red team head to arena {field_num} now\n"
                messageb = f"blue team head to arena {field_num} now\n"        
                formatted =  f"{TeamAObject.pid}|{urgency}|{messager}{TeamBObject.pid}|{urgency}|{messager}{TeamCObject.pid}|{urgency}|{messageb}{TeamDObject.pid}|{urgency}|{messageb}"
            case "parts":
                message = f"parts request approved\n"
                formatted = f"{TeamAObject.pid}|{urgency}|{message}{TeamBObject.pid}|{urgency}|{message}{TeamCObject.pid}|{urgency}|{message}{TeamDObject.pid}|{urgency}|{message}"
                
        self.ui.Errorbox.clear()
        self.ui.Errorbox.insertPlainText(formatted)

        self.radio.send_message(TeamAObject.pid, TeamBObject.pid,TeamCObject.pid,TeamDObject.pid,urgency,type)
      
    #single message
    def send_message_single(self):

        TeamFObject=(self.ui.TeamF_box.itemData(self.ui.TeamF_box.currentIndex()))

        field_num = (self.ui.Arena_select.currentText())
        print(str(field_num))
        intensity_val = self.ui.Intensity.currentIndex() #intensity value is based on the array index becuase idk how to get the text value and this works fine ish
        print(f"intensity value = {intensity_val}\n")

        match intensity_val:
            case 2: #parts
                intensity = self.urgency[3]
                type = "parts"
            case 1: #high
                intensity = self.urgency[2]
                type = "high"
            case 0: #low
                intensity = self.urgency[1]
                type = "default"
            case _: #default
                intensity = self.urgency[0]
                type = "default"
        match type:
            case "default":
                message = f"head to arena {field_num} now\n"
                formatted = f"{TeamFObject.pid}|{intensity}|{message}"
            case "high":
                message = f"head to arena {field_num} now\n"
                formatted = f"{TeamFObject.pid}|{intensity}|{message}"
            case "Parts":
                message = f"parts request approved\n"
                formatted = f"{TeamFObject.pid}|{intensity}|{message}"
        self.ui.Errorbox.clear()
        self.ui.Errorbox.insertPlainText(formatted)
        self.radio.send_message_single(TeamFObject.pid,field_num,intensity,type)


    #functions for automatic mode
    #Automatic Mode - Polling Functions to stay within rate limits and check for queue changes
    def toggle_automatic_mode(self, checked):
        if checked:
            self.poll_interval_ms = 30000  # 15 seconds (change to 30 for actual match time)
            self.last_queue_signature = None
            self.api_cooldown_until = 0
            self.poll_timer.start(self.poll_interval_ms)
            self.poll_for_queue_changes()  # Initial call to populate immediately
            self.ui.Automatic_indicator.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        else:
            self.poll_timer.stop()
            print("Automatic mode stopped, timer halted")
            self.ui.Automatic_indicator.setPixmap(QtGui.QPixmap(ICON_RED_LED))

    def poll_for_queue_changes(self):
        #Setting Initial Timer
        now = time.time()
        if now < self.api_cooldown_until:
            print("In cooldown, skipping API call")
            return
        
        #API Calls to get active match and queue details
        active_match_details = ftclive_queueteams.get_active_match_details()
        queue_details = ftclive_queueteams.get_queue_match_details()
        if not active_match_details or not queue_details:
            self.api_cooldown_until = now + 60  # Back off for 60 seconds
            return

        queue_signature = self.generate_queue_signature(queue_details)
        teams_to_queue = self.extract_teams_from_queue(queue_details)
        field_num = self.extract_field_from_queue(queue_details)
        match_number = queue_details["matchBrief"]["matchNumber"]

        #Show Qualification Number in UI
        self.ui.qualNumText.clear()
        self.ui.qualNumText.insertPlainText(str(match_number))

        #Show Teams to Queue in UI Text Boxes
        print ("Teams to queue:", teams_to_queue)
        red1, red2, blue1, blue2 = map(str, teams_to_queue)  # Ensure all team names are strings
        self.ui.redTeam1Text.clear()
        self.ui.redTeam2Text.clear()
        self.ui.blueTeam1Text.clear()
        self.ui.blueTeam2Text.clear()
        self.ui.redTeam1Text.insertPlainText(red1)
        self.ui.redTeam2Text.insertPlainText(red2)
        self.ui.blueTeam1Text.insertPlainText(blue1)
        self.ui.blueTeam2Text.insertPlainText(blue2)

        #Show Field # in UI
        self.ui.fieldNumText.clear()
        self.ui.fieldNumText.insertPlainText(str(field_num))
        # for team in self.teams:
        #     print(f"  team.name={team.name!r}, type={type(team.name)}, pid={team.pid!r}, match={team.name in teams_to_queue}")
        teams_to_queue_pid = [team.pid for team in self.teams if team.name in teams_to_queue]
        print("teams_to_queue_pid:", teams_to_queue_pid)  

        #If the queue signature has changed since last poll, send new messages to new teams in queue
        if queue_signature != self.last_queue_signature:
            print("Queue changed, sending messages")
            self.last_queue_signature = queue_signature
            intensity = "FFFF00"
            self.radio.send_message(teams_to_queue_pid[0], teams_to_queue_pid[1], teams_to_queue_pid[2], teams_to_queue_pid[3], field_num, "FFFF00")
            messager = f"red team head to arena {field_num}\n"
            messageb = f"blue team head to arena {field_num}\n"        
            formatted =  f"{teams_to_queue_pid[0]}|{intensity}|{messager}{teams_to_queue_pid[1]}|{intensity}|{messager}{teams_to_queue_pid[2]}|{intensity}|{messageb}{teams_to_queue_pid[3]}|{intensity}|{messageb}"
            self.ui.Errorbox.clear()
            self.ui.Errorbox.insertPlainText(formatted)
        else:
            #If Match State turns to "REVIEW" send a red message to teams:
            match_state = self.extract_match_state_from_queue(active_match_details)
            self.ui.matchStateText.clear()
            self.ui.matchStateText.insertPlainText(match_state)
            print(f"Match state: {match_state}")
            if (match_state == "REVIEW"):
                intensity = "FF0000"
                self.api_cooldown_until = now + 60  # Back off for 60 seconds to avoid spamming during review 
                self.radio.send_message(teams_to_queue_pid[0], teams_to_queue_pid[1], teams_to_queue_pid[2], teams_to_queue_pid[3], field_num, "FF0000")
                messager = f"red team head to arena {field_num}\n"
                messageb = f"blue team head to arena {field_num}\n"        
                formatted =  f"{teams_to_queue_pid[0]}|{intensity}|{messager}{teams_to_queue_pid[1]}|{intensity}|{messager}{teams_to_queue_pid[2]}|{intensity}|{messageb}{teams_to_queue_pid[3]}|{intensity}|{messageb}"
                self.ui.Errorbox.clear()
                self.ui.Errorbox.insertPlainText(formatted)
                 

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

    def extract_match_state_from_queue(self, active_match_details):
        return active_match_details["matches"][0].get("matchState")
    
    def extract_field_from_queue(self, queue_details):
        return queue_details["matchBrief"].get("field")
        
# Run application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
