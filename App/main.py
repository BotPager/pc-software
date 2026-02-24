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
import time
import numpy as np
from ui_PCUI import Ui_MainWindow
from teams import Team
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
import os
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Universal"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface = None
        self.is_connecting = False  # The gatekeeper flag
        #init threadding
        self.threadpool = QThreadPool()
        #debug things i think
        # thread_count = self.threadpool.maxThreadCount()
        # print(f"Multithreading with maximum {thread_count} threads")
        pub.subscribe(self.onDisconnect, "meshtastic.connection.lost")
        pub.subscribe(self.onConnection, "meshtastic.connection.established")

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #always load to inputting pagers
        self.ui.stackedWidget.setCurrentIndex(0)

        self.teams = []  # list to hold Team objects
        self.load_teams_from_file()
        self.setup_mesh()


       


        # Connect page switches
        self.ui.SwitchManual.clicked.connect(self.show_manual_page)
        self.ui.SwitchPager.clicked.connect(self.show_set_pagers_page)
        self.ui.SwitchAuto.clicked.connect(self.show_automatic_page)

        # connect to team loading button
        self.ui.pushButton_2.clicked.connect(self.collect_team_data)

        #connect to send message butotn
        self.ui.MessageTeam.clicked.connect(self.send_message_manual)

          

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

            self.check_valid(team_name,pid)
        self.set_teams()

    # After loading all valid teams
    def set_teams(self):
        self.ui.TeamA_box.clear()
        self.ui.TeamB_box.clear()

        for team in self.teams:
            # Add team name (or format it nicely)
            self.ui.TeamA_box.addItem(team.name,team)
            self.ui.TeamB_box.addItem(team.name,team)

        self.print_teams()


#debug info probably for what teams are validly loaded
    def print_teams(self):
        if len(self.teams) != 0:
            print("Valid teams loaded:")
            for t in self.teams:
                print(t)
                self.save_teams()
        else:
            print("no valid teams")
#code used when loading teams to verify no duplicated and to skip empty lines
    def check_valid(self,team_name,pid):
        # Skip empty rows
        if team_name == "" or pid == "":
            return

        # Validate team number
        if not (team_name.isdigit() and 1 <= int(team_name) <= 99999):
            print(f"Invalid TeamN: {team_name}")
            return

        # Validate PID (4 hex characters)
        if not (len(pid) == 4 and all(c in "0123456789abcdefABCDEF" for c in pid)):
            print(f"Invalid PID: {pid}")
            return
        #check duplicate team number or duplicate pid
        new_team = Team(team_name,pid)

        if any(t.name == new_team.name for t in self.teams):
            print(f"skipping duplicate team '{new_team.name}'")
            return
        if any(t.pid == new_team.pid for t in self.teams):
            print(f"skipping duplicate team 'new_team.pid'")
            return

        # Create and add Team object
        self.teams.append(new_team)
#save teams when we click load teams
    def save_teams(self):
        #get data to list
        # convert to numpy array
        team_data = [[t.name, t.pid] for t in self.teams]
        converted_array = np.array(team_data)
        np.savetxt("teams.txt",converted_array,delimiter=",",fmt='%s') 
# loading teams from file into pc ui
    #loads into the teams object for use on manual mode only
    def load_teams_from_file(self):
        if not os.path.exists("teams.txt"):
            print("error teams.txt file missing\n either set teams or download a teams.txt and rerun software\n")
            return
        # get data from file
        # read line by line
        with open("teams.txt") as f:
            for x in f:
               #strip
               x = x.strip('\n')
               # index 0 = teamnumber
               # index 1 = pid
               a = x.split(",",2)
               #validation
               self.check_valid(a[0],a[1])
        f.close()
        self.set_teams()
        self.display_loaded()
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








                     



    #meshtastic code
    #start the connection to the meshtastic gateway
    #now rewritten to not pause the ui
    #handles disconnects as well

    def setup_mesh(self):
        if self.is_connecting:
            return
        else:
            self.is_connecting = True
        def connection_task():
            #try to connect to device if this doesnt work (it uses the tty interface instead retry)
            while self.is_connecting:
                try:
                    print("connecting")
                    self.interface = meshtastic.serial_interface.SerialInterface()
                    print(self.interface)
                    if self.interface.devPath:
                        break
                    else:
                        self.interface.close()
                except Exception as e:
                    print("Error device not connected\n")
                    print(f"trying again in 3 seconds {e}")
                    time.sleep(3)

        worker = Worker(connection_task)
        self.threadpool.start(worker)


    def onConnection(self, interface, topic=pub.AUTO_TOPIC):
        print("connected")
        self.is_connecting = False

    def onDisconnect(self, interface, topic=pub.AUTO_TOPIC):
        print("disconnection occurred please recconnect")
        self.is_connecting = False
        if self.interface:
            try:
                self.interface.close()
            except:
                pass
            self.interface = None

        self.setup_mesh()
    #message sending manual mode
    #get the object from the currently selected team number (read index of current selection)
        #team a right
        #team b left
    #automatic may just use result from api matched against the array teams?
    def send_message_manual(self):
        #get data from currently selected teams
        TeamAObject=(self.ui.TeamB_box.itemData(self.ui.TeamB_box.currentIndex()))
        TeamBObject=(self.ui.TeamA_box.itemData(self.ui.TeamA_box.currentIndex()))

        TeamBName = TeamBObject.name
        TeamAName = TeamAObject.name

        #need to add check to make sure names arent duplicates
        #if teama.name  == teamb.name  error and show message
        worker = Worker(self.send_message, TeamAObject.pid,TeamBObject.pid)
        self.threadpool.start(worker)
        # self.send_message(TeamAPID,TeamBPID)

    #should be reusable for automatic mode
    #maybe needs to be changed slightly? but the message format makes sense.
    #just combine strings and then send result over meshtastic api call
    def send_message(self, TeamAPID, TeamBPID):
        print("sending")
        message = "|go to pit"
        messageTeamA = TeamAPID + message;
        messageTeamB = TeamBPID + message;
        #error handling for pager disconnection during send
        sent = False
        while not sent:
            while self.interface is None or self.is_connecting:
                print("sending sent waiting for connection to device")
                time.sleep(5)
            try:
                self.interface.sendText(messageTeamA)
                time.sleep(5)
                self.interface.sendText(messageTeamB)
                sent = True
            except Exception as e:
                print(" sending failed due to {e}\n device disconnected \n sending paused to recconnection")
                sent = False
                time.sleep(2)


# Run application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
