# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PCUIMxeaIV.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1038, 841)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setGeometry(QRect(10, 10, 781, 80))
        self.horizontalFrame.setMaximumSize(QSize(1920, 200))
        self.TopBar = QHBoxLayout(self.horizontalFrame)
        self.TopBar.setObjectName(u"TopBar")
        self.frame = QFrame(self.horizontalFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet(u"#frame{\n"
"border-radius: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 30, 81, 16))

        self.TopBar.addWidget(self.frame)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setGeometry(QRect(9, 89, 781, 461))
        self.Content.setMaximumSize(QSize(1920, 16777215))
        self.Content.setFrameShape(QFrame.Shape.StyledPanel)
        self.Content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalFrame_2 = QFrame(self.Content)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setGeometry(QRect(0, 0, 781, 461))
        self.horizontalFrame_2.setAutoFillBackground(True)
        self.horizontalFrame_2.setStyleSheet(u"#horizontalFrame_2{\n"
"	border-radius: 0px;\n"
"}")
        self.horizontalFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Menu_selectors = QFrame(self.horizontalFrame_2)
        self.Menu_selectors.setObjectName(u"Menu_selectors")
        self.Menu_selectors.setMaximumSize(QSize(100, 16777215))
        self.Menu_selectors.setFrameShape(QFrame.Shape.WinPanel)
        self.verticalLayout_2 = QVBoxLayout(self.Menu_selectors)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalFrame_2 = QFrame(self.Menu_selectors)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_4 = QPushButton(self.verticalFrame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.SwitchAuto = QPushButton(self.verticalFrame_2)
        self.SwitchAuto.setObjectName(u"SwitchAuto")

        self.verticalLayout_5.addWidget(self.SwitchAuto)

        self.SwitchPager = QPushButton(self.verticalFrame_2)
        self.SwitchPager.setObjectName(u"SwitchPager")

        self.verticalLayout_5.addWidget(self.SwitchPager)


        self.verticalLayout_2.addWidget(self.verticalFrame_2)

        self.frame_2 = QFrame(self.Menu_selectors)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.Menu_selectors)

        self.Main_Menus = QFrame(self.horizontalFrame_2)
        self.Main_Menus.setObjectName(u"Main_Menus")
        self.Main_Menus.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout = QVBoxLayout(self.Main_Menus)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.stackedWidget = QStackedWidget(self.Main_Menus)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(True)
        self.Manual = QWidget()
        self.Manual.setObjectName(u"Manual")
        self.horizontalLayoutWidget = QWidget(self.Manual)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 170, 206, 106))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ManualIcons = QFrame(self.horizontalLayoutWidget)
        self.ManualIcons.setObjectName(u"ManualIcons")
        self.verticalLayout_6 = QVBoxLayout(self.ManualIcons)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Title = QLabel(self.ManualIcons)
        self.Title.setObjectName(u"Title")

        self.verticalLayout_6.addWidget(self.Title)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.TeamA = QLabel(self.ManualIcons)
        self.TeamA.setObjectName(u"TeamA")
        self.TeamA.setMinimumSize(QSize(81, 16))

        self.gridLayout.addWidget(self.TeamA, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.ManualIcons)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.TeamB = QLabel(self.ManualIcons)
        self.TeamB.setObjectName(u"TeamB")
        self.TeamB.setMinimumSize(QSize(81, 16))

        self.gridLayout.addWidget(self.TeamB, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.ManualIcons)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.ManualIcons)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addWidget(self.ManualIcons)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.stackedWidget.addWidget(self.Manual)
        self.Set_teams = QWidget()
        self.Set_teams.setObjectName(u"Set_teams")
        self.stackedWidget.addWidget(self.Set_teams)
        self.Automatic = QWidget()
        self.Automatic.setObjectName(u"Automatic")
        self.stackedWidget.addWidget(self.Automatic)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Main_Menus)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pager Software", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.SwitchAuto.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.SwitchPager.setText(QCoreApplication.translate("MainWindow", u"Set Pagers", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"            MANUAL QUEUE", None))
        self.TeamA.setText(QCoreApplication.translate("MainWindow", u"Select Team A", None))
        self.TeamB.setText(QCoreApplication.translate("MainWindow", u"Select Team B", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Message Team", None))
    # retranslateUi

