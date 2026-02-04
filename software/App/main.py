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
from ui_PCUI import Ui_MainWindow
from teams import Team
import meshtastic
import meshtastic.serial_interface
from pubsub import pub

class Worker(QRunnable):
    """Worker thread.

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread.
                     Supplied args and kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    """

    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        """Initialise the runner function with passed args, kwargs."""
        self.fn(*self.args, **self.kwargs)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface = None
        self.is_connecting = False  # The gatekeeper flag
        #init threadding
        self.threadpool = QThreadPool()
        #debug things i think
        thread_count = self.threadpool.maxThreadCount()
        print(f"Multithreading with maximum {thread_count} threads")
        pub.subscribe(self.onDisconnect, "meshtastic.connection.lost")
        pub.subscribe(self.onConnection, "meshtastic.connection.established")
        self.setup_mesh()
        self.teams = []  # list to hold Team objects



        
        
        # Load UI

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #always load to inputting pagers
        self.ui.stackedWidget.setCurrentIndex(0)

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
        for i in range(0, 17):
            team_widget = getattr(self.ui, f"TeamN{i}", None)
            pid_widget = getattr(self.ui, f"PID{i}", None)

            if not team_widget or not pid_widget:
                continue

            team_name = team_widget.text().strip()
            pid = pid_widget.text().strip()

            # Skip empty rows
            if team_name == "" or pid == "":
                continue

            # Validate team number
            if not (team_name.isdigit() and 1 <= int(team_name) <= 9999):
                print(f"Invalid TeamN{i}: {team_name}")
                continue

            # Validate PID (4 hex characters)
            if not (len(pid) == 4 and all(c in "0123456789abcdefABCDEF" for c in pid)):
                print(f"Invalid PID{i}: {pid}")
                continue

            # Create and add Team object
            self.teams.append(Team(team_name, pid))

            # After loading all valid teams
            self.ui.TeamA_box.clear()
            self.ui.TeamB_box.clear()

            for team in self.teams:
                # Add team name (or format it nicely)
                self.ui.TeamA_box.addItem(team.name,team)
                self.ui.TeamB_box.addItem(team.name,team)

        print("Valid teams loaded:")
        for t in self.teams:
            print(t)


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
                    print(f"trying again in 1 seconds {e}")
                    time.sleep(1)

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
        worker = Worker(self.send_message, TeamAObject.pid,TeamAObject.pid)
        self.threadpool.start(worker)
        # self.send_message(TeamAPID,TeamBPID)

    #should be reusable for automatic mode
    #maybe needs to be changed slightly? but the message format makes sense.
    #just combine strings and then send result over meshtastic api call
    def send_message(self, TeamAPID, TeamBPID):
        message = "|go to pit"
        messageTeamA = TeamAPID + message;
        messageTeamB = TeamBPID + message;

        self.interface.sendText(messageTeamA)
        #arbitrary needs to be tested to see how long is actually needed
        time.sleep(5)
        self.interface.sendText(messageTeamB)

        
# Run application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
