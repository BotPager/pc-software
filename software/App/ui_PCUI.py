# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PCUI.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

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
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"#frame{\n"
"border-radius: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 30, 131, 16))

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
        self.horizontalFrame_2.setAutoFillBackground(False)
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
        self.SwitchPager = QPushButton(self.verticalFrame_2)
        self.SwitchPager.setObjectName(u"SwitchPager")

        self.verticalLayout_5.addWidget(self.SwitchPager)

        self.SwitchManual = QPushButton(self.verticalFrame_2)
        self.SwitchManual.setObjectName(u"SwitchManual")

        self.verticalLayout_5.addWidget(self.SwitchManual)

        self.SwitchAuto = QPushButton(self.verticalFrame_2)
        self.SwitchAuto.setObjectName(u"SwitchAuto")

        self.verticalLayout_5.addWidget(self.SwitchAuto)


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
        self.SetTeams = QWidget()
        self.SetTeams.setObjectName(u"SetTeams")
        self.TeamTitleLable = QLabel(self.SetTeams)
        self.TeamTitleLable.setObjectName(u"TeamTitleLable")
        self.TeamTitleLable.setGeometry(QRect(310, 60, 131, 16))
        self.horizontalLayoutWidget_3 = QWidget(self.SetTeams)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(190, 90, 391, 283))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BlockForTeamSet1 = QVBoxLayout()
        self.BlockForTeamSet1.setObjectName(u"BlockForTeamSet1")
        self.Textlabels_1 = QHBoxLayout()
        self.Textlabels_1.setObjectName(u"Textlabels_1")
        self.PagerID1 = QLabel(self.horizontalLayoutWidget_3)
        self.PagerID1.setObjectName(u"PagerID1")

        self.Textlabels_1.addWidget(self.PagerID1)

        self.line = QFrame(self.horizontalLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.Textlabels_1.addWidget(self.line)

        self.label_4 = QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.Textlabels_1.addWidget(self.label_4)


        self.BlockForTeamSet1.addLayout(self.Textlabels_1)

        self.TeamBlock1 = QGridLayout()
        self.TeamBlock1.setObjectName(u"TeamBlock1")
        self.PID1 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID1.setObjectName(u"PID1")

        self.TeamBlock1.addWidget(self.PID1, 0, 1, 1, 1)

        self.TeamN4 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN4.setObjectName(u"TeamN4")

        self.TeamBlock1.addWidget(self.TeamN4, 3, 0, 1, 1)

        self.PID3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID3.setObjectName(u"PID3")

        self.TeamBlock1.addWidget(self.PID3, 2, 1, 1, 1)

        self.PID2 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID2.setObjectName(u"PID2")

        self.TeamBlock1.addWidget(self.PID2, 1, 1, 1, 1)

        self.TeamN7 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN7.setObjectName(u"TeamN7")

        self.TeamBlock1.addWidget(self.TeamN7, 6, 0, 1, 1)

        self.TeamN3 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN3.setObjectName(u"TeamN3")

        self.TeamBlock1.addWidget(self.TeamN3, 2, 0, 1, 1)

        self.PID4 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID4.setObjectName(u"PID4")

        self.TeamBlock1.addWidget(self.PID4, 3, 1, 1, 1)

        self.TeamN1 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN1.setObjectName(u"TeamN1")

        self.TeamBlock1.addWidget(self.TeamN1, 0, 0, 1, 1)

        self.PID6 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID6.setObjectName(u"PID6")

        self.TeamBlock1.addWidget(self.PID6, 5, 1, 1, 1)

        self.TeamN5 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN5.setObjectName(u"TeamN5")

        self.TeamBlock1.addWidget(self.TeamN5, 4, 0, 1, 1)

        self.PID5 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID5.setObjectName(u"PID5")

        self.TeamBlock1.addWidget(self.PID5, 4, 1, 1, 1)

        self.TeamN6 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN6.setObjectName(u"TeamN6")

        self.TeamBlock1.addWidget(self.TeamN6, 5, 0, 1, 1)

        self.TeamN2 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN2.setObjectName(u"TeamN2")

        self.TeamBlock1.addWidget(self.TeamN2, 1, 0, 1, 1)

        self.TeamN8 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN8.setObjectName(u"TeamN8")

        self.TeamBlock1.addWidget(self.TeamN8, 7, 0, 1, 1)

        self.PID7 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID7.setObjectName(u"PID7")

        self.TeamBlock1.addWidget(self.PID7, 6, 1, 1, 1)

        self.PID8 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID8.setObjectName(u"PID8")

        self.TeamBlock1.addWidget(self.PID8, 7, 1, 1, 1)


        self.BlockForTeamSet1.addLayout(self.TeamBlock1)


        self.horizontalLayout_3.addLayout(self.BlockForTeamSet1)

        self.line_3 = QFrame(self.horizontalLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.BlockForTeamSet2 = QVBoxLayout()
        self.BlockForTeamSet2.setObjectName(u"BlockForTeamSet2")
        self.Textlabels_2 = QHBoxLayout()
        self.Textlabels_2.setObjectName(u"Textlabels_2")
        self.PagerID1_2 = QLabel(self.horizontalLayoutWidget_3)
        self.PagerID1_2.setObjectName(u"PagerID1_2")

        self.Textlabels_2.addWidget(self.PagerID1_2)

        self.line_2 = QFrame(self.horizontalLayoutWidget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.Textlabels_2.addWidget(self.line_2)

        self.label_5 = QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.Textlabels_2.addWidget(self.label_5)


        self.BlockForTeamSet2.addLayout(self.Textlabels_2)

        self.TeamBlock2 = QGridLayout()
        self.TeamBlock2.setObjectName(u"TeamBlock2")
        self.PID9 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID9.setObjectName(u"PID9")

        self.TeamBlock2.addWidget(self.PID9, 0, 1, 1, 1)

        self.TeamN12 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN12.setObjectName(u"TeamN12")

        self.TeamBlock2.addWidget(self.TeamN12, 3, 0, 1, 1)

        self.PID11 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID11.setObjectName(u"PID11")

        self.TeamBlock2.addWidget(self.PID11, 2, 1, 1, 1)

        self.PID10 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID10.setObjectName(u"PID10")

        self.TeamBlock2.addWidget(self.PID10, 1, 1, 1, 1)

        self.TeamN15 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN15.setObjectName(u"TeamN15")

        self.TeamBlock2.addWidget(self.TeamN15, 6, 0, 1, 1)

        self.TeamN11 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN11.setObjectName(u"TeamN11")

        self.TeamBlock2.addWidget(self.TeamN11, 2, 0, 1, 1)

        self.PID12 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID12.setObjectName(u"PID12")

        self.TeamBlock2.addWidget(self.PID12, 3, 1, 1, 1)

        self.TeamN9 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN9.setObjectName(u"TeamN9")

        self.TeamBlock2.addWidget(self.TeamN9, 0, 0, 1, 1)

        self.PID14 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID14.setObjectName(u"PID14")

        self.TeamBlock2.addWidget(self.PID14, 5, 1, 1, 1)

        self.TeamN13 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN13.setObjectName(u"TeamN13")

        self.TeamBlock2.addWidget(self.TeamN13, 4, 0, 1, 1)

        self.PID13 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID13.setObjectName(u"PID13")

        self.TeamBlock2.addWidget(self.PID13, 4, 1, 1, 1)

        self.TeamN14 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN14.setObjectName(u"TeamN14")

        self.TeamBlock2.addWidget(self.TeamN14, 5, 0, 1, 1)

        self.TeamN10 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN10.setObjectName(u"TeamN10")

        self.TeamBlock2.addWidget(self.TeamN10, 1, 0, 1, 1)

        self.TeamN16 = QLineEdit(self.horizontalLayoutWidget_3)
        self.TeamN16.setObjectName(u"TeamN16")

        self.TeamBlock2.addWidget(self.TeamN16, 7, 0, 1, 1)

        self.PID15 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID15.setObjectName(u"PID15")

        self.TeamBlock2.addWidget(self.PID15, 6, 1, 1, 1)

        self.PID16 = QLineEdit(self.horizontalLayoutWidget_3)
        self.PID16.setObjectName(u"PID16")

        self.TeamBlock2.addWidget(self.PID16, 7, 1, 1, 1)


        self.BlockForTeamSet2.addLayout(self.TeamBlock2)


        self.horizontalLayout_3.addLayout(self.BlockForTeamSet2)

        self.label_2 = QLabel(self.SetTeams)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 360, 49, 16))
        self.pushButton_2 = QPushButton(self.SetTeams)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 380, 121, 24))
        self.stackedWidget.addWidget(self.SetTeams)
        self.Manual = QWidget()
        self.Manual.setObjectName(u"Manual")
        self.horizontalLayoutWidget = QWidget(self.Manual)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 170, 210, 122))
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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pager Software", None))
        self.SwitchPager.setText(QCoreApplication.translate("MainWindow", u"Set Pagers", None))
        self.SwitchManual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.SwitchAuto.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.TeamTitleLable.setText(QCoreApplication.translate("MainWindow", u"Enter Team Info", None))
        self.PagerID1.setText(QCoreApplication.translate("MainWindow", u"Team Number", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pager ID", None))
        self.PagerID1_2.setText(QCoreApplication.translate("MainWindow", u"Team Number", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pager ID", None))
        self.label_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Set teams", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"            MANUAL QUEUE", None))
        self.TeamA.setText(QCoreApplication.translate("MainWindow", u"Select Team A", None))
        self.TeamB.setText(QCoreApplication.translate("MainWindow", u"Select Team B", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Message Team", None))
    # retranslateUi

