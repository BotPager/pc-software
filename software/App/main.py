from PySide6.QtWidgets import QApplication, QMainWindow
from ui_PCUI import Ui_MainWindow
from teams import Team
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect page switches
        self.ui.SwitchManual.clicked.connect(self.show_manual_page)
        self.ui.SwitchPager.clicked.connect(self.show_set_pagers_page)
        self.ui.SwitchAuto.clicked.connect(self.show_automatic_page)

        # CONNECT YOUR TEAM LOADING BUTTON HERE
        self.ui.pushButton_2.clicked.connect(self.collect_team_data)
        # self.ui.pushButton.clicked.connect()

    # -------------------------
    # Page switching functions
    # -------------------------
    def show_manual_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_set_pagers_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_automatic_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    # -------------------------
    # TEAM DATA COLLECTION
    # -------------------------
    def collect_team_data(self):
        self.teams = []  # list to hold Team objects

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
            self.ui.comboBox.clear()
            self.ui.comboBox_2.clear()

            for team in self.teams:
                # Add team name (or format it nicely)
                self.ui.comboBox.addItem(team.name)
                self.ui.comboBox_2.addItem(team.name)

        print("Valid teams loaded:")
        for t in self.teams:
            print(t)



# Run application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
