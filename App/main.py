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
from worker import Worker
from comms import *
import time
import numpy as np
from ui_PCUI import Ui_MainWindow
import teams
import subprocess
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #always load to inputting pagers
        self.ui.stackedWidget.setCurrentIndex(0)
        #load teams
        #
        self.teams = teams.create_teams()
        self.teams = teams.load_teams_from_file("teams.txt",self.teams)
        self.display_loaded()


        
        # Init Radio Communication
        self.radio = MeshGateway()
        self.radio.connect()
       
        self.ui.load_teams.clicked.connect(lambda: self.open_file_picker("teams",self.teams))
        self.ui.load_pid.clicked.connect(lambda: self.open_file_picker("pid",self.teams))

        # Connect page switches
        self.ui.SwitchManual.clicked.connect(self.show_manual_page)
        self.ui.SwitchPager.clicked.connect(self.show_set_pagers_page)
        self.ui.SwitchAuto.clicked.connect(self.show_automatic_page)

        # connect to team loading button
        self.ui.pushButton_2.clicked.connect(self.collect_team_data)
        self.ui.pushButton.clicked.connect(self.display_teams_automatic)

        #connect to send message butotn
        self.ui.MessageTeam.clicked.connect(self.send_message_manual)
        self.ui.pushButton_3.clicked.connect(self.close)
          

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
            if team_widget.text().strip() == "-" or pid_widget.text().strip() == "-":
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

        for team in self.teams:
            # Add team name (or format it nicely)
            self.ui.TeamA_box.addItem(team.name,team)
            self.ui.TeamB_box.addItem(team.name,team)
            self.ui.TeamC_box.addItem(team.name,team)
            self.ui.TeamD_box.addItem(team.name,team)
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
    #show loaded teams on the editable textbox
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


    def open_file_picker(self, file_type,team_list):
        print("file picker")
        # Define filters based on what you're looking for
        file_filter = "Text Files (*.txt);;All Files (*)"
        caption = "Select Teams File" if file_type == "teams" else "Select PID File"

        # Open the native dialog
        file_path, _ = QFileDialog.getOpenFileName(self, caption, "", file_filter)

        if file_path:
            if file_type == "teams":
                # Load the teams and refresh the UI display
                print(f"Loading teams from: {file_path}")
                # self.teams = teams.load_teams_from_file(file_path)
                # self.display_loaded()
                # self.set_teams() # Update the ComboBoxes too
            
            elif file_type == "pid":
                # If you want to handle the pid file specifically
                print(f"PID file selected: {file_path}")
                print(f"PIDS:")
                pids = teams.load_pid(file_path)
                for i in range(0,len(pids)):
                    team_list[i].pid = pids[i]
                    
                print(teams.load_pid(file_path))
                
                # You could call teams.load(file_path) here if needed


    #message sending manual mode
    #get the object from the currently selected team number (read index of current selection)
        #team a right
        #team b left
    #automatic may just use result from api matched against the array teams?
    def send_message_manual(self):
        #get data from currently selected teams
        TeamAObject=(self.ui.TeamB_box.itemData(self.ui.TeamA_box.currentIndex()))
        TeamBObject=(self.ui.TeamA_box.itemData(self.ui.TeamB_box.currentIndex()))
        TeamCObject=(self.ui.TeamC_box.itemData(self.ui.TeamC_box.currentIndex()))
        TeamDObject=(self.ui.TeamD_box.itemData(self.ui.TeamD_box.currentIndex()))
        self.radio.send_message(TeamAObject.pid, TeamBObject.pid,TeamCObject.pid,TeamDObject.pid)

    def display_teams_automatic(self):
        """Load and display teams from team_numbers.txt on the automatic page"""
        print("Fetching latest teams from API...")
        try:
            result = subprocess.run(
                ["python", "ftclive_polling.py"],  # On Windows, use "python" not "python3"
                capture_output=True,
                text=True,
                timeout=10  # 10 second timeout
            )
            
            if result.returncode == 0:
                print("✓ Team data updated successfully")
                print(result.stdout)  # Show the output from ftclive_polling.py
            else:
                print(f"⚠ Warning: ftclive_polling.py had errors:\n{result.stderr}")
        
        except subprocess.TimeoutExpired:
            print("⚠ Warning: API request timed out")
        except Exception as e:
            print(f"⚠ Warning: Could not run ftclive_polling.py: {e}")
    
        team_numbers = teams.load_team_number("team_numbers.txt")
        
        if not team_numbers:
            self.ui.label_3.setText("No teams found in team_numbers.txt")
            print("No teams found in team_numbers.txt")
            return
        
        # Format teams for display (show first 10, then indicate if more)
        if len(team_numbers) <= 10:
            teams_text = f"Teams ({len(team_numbers)}):\n" + ", ".join(team_numbers)
        else:
            teams_text = f"Teams ({len(team_numbers)}):\n"
            teams_text += ", ".join(team_numbers[:10])
            teams_text += f"... (+{len(team_numbers) - 10} more)"
        
        self.ui.label_3.setText(teams_text)
        print(f"✓ Loaded {len(team_numbers)} teams from team_numbers.txt")
        
# Run application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
