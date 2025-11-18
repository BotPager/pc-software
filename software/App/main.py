from PySide6.QtWidgets import QApplication, QMainWindow
from ui_PCUI import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect your buttons to stacked widget
        self.ui.pushButton_4.clicked.connect(self.show_manual_page)
        self.ui.SwitchPager.clicked.connect(self.show_set_pagers_page)
        self.ui.SwitchAuto.clicked.connect(self.show_automatic_page)

    # --- Page switching functions ---
    def show_manual_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_set_pagers_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_automatic_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

# Run application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
