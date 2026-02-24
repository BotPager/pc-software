from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import (
         QRunnable,
         QThreadPool,
         QTimer,
         Slot
    )
from worker import Worker
from comms import *
import time
import numpy as np
from ui_PCUI import Ui_MainWindow
import teams
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
import os
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Universal"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
   
        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #always load to inputting pagers
        self.ui.stackedWidget.setCurrentIndex(0)
        #load teams
        self.teams = teams.load_teams_from_file()
        self.display_loaded()
        # Init Radio Communication
        self.radio = MeshGateway()
        self.radio.connect()
       


        # Connect page switches
        self.ui.SwitchManual.clicked.connect(self.show_manual_page)
        self.ui.SwitchPager.clicked.connect(self.show_set_pagers_page)
        self.ui.SwitchAuto.clicked.connect(self.show_automatic_page)

        # connect to team loading button
        self.ui.pushButton_2.clicked.connect(self.collect_team_data)

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
        self.teams.clear()
        for i in range(0, 16):
            team_widget = getattr(self.ui, f"TeamN{i}", None)
            pid_widget = getattr(self.ui, f"PID{i}", None)

            if not team_widget or not pid_widget:
                continue

            team_name = team_widget.text().strip()
            pid = pid_widget.text().strip()
            new_team = teams.check_valid(team_name, pid, self.teams_list)
            if new_team:
                self.teams.append(new_team)
        teams.save_teams_to_file(self.teams_list)
        self.set_teams()
   
    # After loading all valid teams
    def set_teams(self):
        self.ui.TeamA_box.clear()
        self.ui.TeamB_box.clear()

        for team in self.teams:
            # Add team name (or format it nicely)
            self.ui.TeamA_box.addItem(team.name,team)
            self.ui.TeamB_box.addItem(team.name,team)
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


    #message sending manual mode
    #get the object from the currently selected team number (read index of current selection)
        #team a right
        #team b left
    #automatic may just use result from api matched against the array teams?
    def send_message_manual(self):
        #get data from currently selected teams
        TeamAObject=(self.ui.TeamB_box.itemData(self.ui.TeamB_box.currentIndex()))
        TeamBObject=(self.ui.TeamA_box.itemData(self.ui.TeamA_box.currentIndex()))
        self.radio.send_message(TeamAObject.pid, TeamBObject.pid)
        
# Run application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
