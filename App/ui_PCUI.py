# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PCUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1038, 841)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setGeometry(QRect(9, 89, 781, 461))
        self.Content.setMaximumSize(QSize(1920, 16777215))
        self.Content.setFrameShape(QFrame.Shape.StyledPanel)
        self.Content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalFrame_2 = QFrame(self.Content)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setGeometry(QRect(0, 0, 781, 461))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy)
        self.horizontalFrame_2.setAutoFillBackground(False)
        self.horizontalFrame_2.setStyleSheet(u"#horizontalFrame_2{\n"
"	border-radius: 0px;\n"
"}")
        self.horizontalFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalFrame_2 = QFrame(self.horizontalFrame_2)
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


        self.horizontalLayout.addWidget(self.verticalFrame_2)

        self.Main_Menus = QFrame(self.horizontalFrame_2)
        self.Main_Menus.setObjectName(u"Main_Menus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Main_Menus.sizePolicy().hasHeightForWidth())
        self.Main_Menus.setSizePolicy(sizePolicy1)
        self.Main_Menus.setMaximumSize(QSize(661, 453))
        self.Main_Menus.setFrameShape(QFrame.Shape.StyledPanel)
        self.Main_Menus.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.Main_Menus)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.stackedWidget = QStackedWidget(self.Main_Menus)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(True)
        self.SetTeams = QWidget()
        self.SetTeams.setObjectName(u"SetTeams")
        self.label_2 = QLabel(self.SetTeams)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 360, 49, 16))
        self.verticalFrame = QFrame(self.SetTeams)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(0, 0, 616, 376))
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.TeamTitleLable = QLabel(self.verticalFrame)
        self.TeamTitleLable.setObjectName(u"TeamTitleLable")

        self.horizontalLayout_5.addWidget(self.TeamTitleLable)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BlockForTeamSet1 = QVBoxLayout()
        self.BlockForTeamSet1.setObjectName(u"BlockForTeamSet1")
        self.Textlabels_1 = QHBoxLayout()
        self.Textlabels_1.setObjectName(u"Textlabels_1")
        self.PagerID1 = QLabel(self.verticalFrame)
        self.PagerID1.setObjectName(u"PagerID1")
        self.PagerID1.setMargin(2)

        self.Textlabels_1.addWidget(self.PagerID1)

        self.line = QFrame(self.verticalFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.Textlabels_1.addWidget(self.line)

        self.label_4 = QLabel(self.verticalFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 0))
        self.label_4.setMargin(2)

        self.Textlabels_1.addWidget(self.label_4)


        self.BlockForTeamSet1.addLayout(self.Textlabels_1)

        self.TeamBlock1 = QGridLayout()
        self.TeamBlock1.setObjectName(u"TeamBlock1")
        self.PID0 = QLineEdit(self.verticalFrame)
        self.PID0.setObjectName(u"PID0")

        self.TeamBlock1.addWidget(self.PID0, 0, 1, 1, 1)

        self.TeamN3 = QLineEdit(self.verticalFrame)
        self.TeamN3.setObjectName(u"TeamN3")

        self.TeamBlock1.addWidget(self.TeamN3, 3, 0, 1, 1)

        self.PID2 = QLineEdit(self.verticalFrame)
        self.PID2.setObjectName(u"PID2")

        self.TeamBlock1.addWidget(self.PID2, 2, 1, 1, 1)

        self.PID1 = QLineEdit(self.verticalFrame)
        self.PID1.setObjectName(u"PID1")

        self.TeamBlock1.addWidget(self.PID1, 1, 1, 1, 1)

        self.TeamN6 = QLineEdit(self.verticalFrame)
        self.TeamN6.setObjectName(u"TeamN6")

        self.TeamBlock1.addWidget(self.TeamN6, 6, 0, 1, 1)

        self.TeamN2 = QLineEdit(self.verticalFrame)
        self.TeamN2.setObjectName(u"TeamN2")

        self.TeamBlock1.addWidget(self.TeamN2, 2, 0, 1, 1)

        self.PID3 = QLineEdit(self.verticalFrame)
        self.PID3.setObjectName(u"PID3")

        self.TeamBlock1.addWidget(self.PID3, 3, 1, 1, 1)

        self.TeamN0 = QLineEdit(self.verticalFrame)
        self.TeamN0.setObjectName(u"TeamN0")

        self.TeamBlock1.addWidget(self.TeamN0, 0, 0, 1, 1)

        self.PID5 = QLineEdit(self.verticalFrame)
        self.PID5.setObjectName(u"PID5")

        self.TeamBlock1.addWidget(self.PID5, 5, 1, 1, 1)

        self.TeamN4 = QLineEdit(self.verticalFrame)
        self.TeamN4.setObjectName(u"TeamN4")

        self.TeamBlock1.addWidget(self.TeamN4, 4, 0, 1, 1)

        self.PID4 = QLineEdit(self.verticalFrame)
        self.PID4.setObjectName(u"PID4")

        self.TeamBlock1.addWidget(self.PID4, 4, 1, 1, 1)

        self.TeamN5 = QLineEdit(self.verticalFrame)
        self.TeamN5.setObjectName(u"TeamN5")

        self.TeamBlock1.addWidget(self.TeamN5, 5, 0, 1, 1)

        self.TeamN1 = QLineEdit(self.verticalFrame)
        self.TeamN1.setObjectName(u"TeamN1")

        self.TeamBlock1.addWidget(self.TeamN1, 1, 0, 1, 1)

        self.TeamN7 = QLineEdit(self.verticalFrame)
        self.TeamN7.setObjectName(u"TeamN7")

        self.TeamBlock1.addWidget(self.TeamN7, 7, 0, 1, 1)

        self.PID6 = QLineEdit(self.verticalFrame)
        self.PID6.setObjectName(u"PID6")

        self.TeamBlock1.addWidget(self.PID6, 6, 1, 1, 1)

        self.PID7 = QLineEdit(self.verticalFrame)
        self.PID7.setObjectName(u"PID7")

        self.TeamBlock1.addWidget(self.PID7, 7, 1, 1, 1)


        self.BlockForTeamSet1.addLayout(self.TeamBlock1)


        self.horizontalLayout_3.addLayout(self.BlockForTeamSet1)

        self.line_3 = QFrame(self.verticalFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.BlockForTeamSet2 = QVBoxLayout()
        self.BlockForTeamSet2.setObjectName(u"BlockForTeamSet2")
        self.Textlabels_2 = QHBoxLayout()
        self.Textlabels_2.setObjectName(u"Textlabels_2")
        self.PagerID1_2 = QLabel(self.verticalFrame)
        self.PagerID1_2.setObjectName(u"PagerID1_2")
        self.PagerID1_2.setMargin(2)

        self.Textlabels_2.addWidget(self.PagerID1_2)

        self.line_2 = QFrame(self.verticalFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.Textlabels_2.addWidget(self.line_2)

        self.label_5 = QLabel(self.verticalFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setMargin(2)

        self.Textlabels_2.addWidget(self.label_5)


        self.BlockForTeamSet2.addLayout(self.Textlabels_2)

        self.TeamBlock2 = QGridLayout()
        self.TeamBlock2.setObjectName(u"TeamBlock2")
        self.PID8 = QLineEdit(self.verticalFrame)
        self.PID8.setObjectName(u"PID8")

        self.TeamBlock2.addWidget(self.PID8, 0, 1, 1, 1)

        self.TeamN11 = QLineEdit(self.verticalFrame)
        self.TeamN11.setObjectName(u"TeamN11")

        self.TeamBlock2.addWidget(self.TeamN11, 3, 0, 1, 1)

        self.PID10 = QLineEdit(self.verticalFrame)
        self.PID10.setObjectName(u"PID10")

        self.TeamBlock2.addWidget(self.PID10, 2, 1, 1, 1)

        self.PID9 = QLineEdit(self.verticalFrame)
        self.PID9.setObjectName(u"PID9")

        self.TeamBlock2.addWidget(self.PID9, 1, 1, 1, 1)

        self.TeamN14 = QLineEdit(self.verticalFrame)
        self.TeamN14.setObjectName(u"TeamN14")

        self.TeamBlock2.addWidget(self.TeamN14, 6, 0, 1, 1)

        self.TeamN10 = QLineEdit(self.verticalFrame)
        self.TeamN10.setObjectName(u"TeamN10")

        self.TeamBlock2.addWidget(self.TeamN10, 2, 0, 1, 1)

        self.PID11 = QLineEdit(self.verticalFrame)
        self.PID11.setObjectName(u"PID11")

        self.TeamBlock2.addWidget(self.PID11, 3, 1, 1, 1)

        self.TeamN8 = QLineEdit(self.verticalFrame)
        self.TeamN8.setObjectName(u"TeamN8")

        self.TeamBlock2.addWidget(self.TeamN8, 0, 0, 1, 1)

        self.PID13 = QLineEdit(self.verticalFrame)
        self.PID13.setObjectName(u"PID13")

        self.TeamBlock2.addWidget(self.PID13, 5, 1, 1, 1)

        self.TeamN12 = QLineEdit(self.verticalFrame)
        self.TeamN12.setObjectName(u"TeamN12")

        self.TeamBlock2.addWidget(self.TeamN12, 4, 0, 1, 1)

        self.PID12 = QLineEdit(self.verticalFrame)
        self.PID12.setObjectName(u"PID12")

        self.TeamBlock2.addWidget(self.PID12, 4, 1, 1, 1)

        self.TeamN13 = QLineEdit(self.verticalFrame)
        self.TeamN13.setObjectName(u"TeamN13")

        self.TeamBlock2.addWidget(self.TeamN13, 5, 0, 1, 1)

        self.TeamN9 = QLineEdit(self.verticalFrame)
        self.TeamN9.setObjectName(u"TeamN9")

        self.TeamBlock2.addWidget(self.TeamN9, 1, 0, 1, 1)

        self.TeamN15 = QLineEdit(self.verticalFrame)
        self.TeamN15.setObjectName(u"TeamN15")

        self.TeamBlock2.addWidget(self.TeamN15, 7, 0, 1, 1)

        self.PID14 = QLineEdit(self.verticalFrame)
        self.PID14.setObjectName(u"PID14")

        self.TeamBlock2.addWidget(self.PID14, 6, 1, 1, 1)

        self.PID15 = QLineEdit(self.verticalFrame)
        self.PID15.setObjectName(u"PID15")

        self.TeamBlock2.addWidget(self.PID15, 7, 1, 1, 1)


        self.BlockForTeamSet2.addLayout(self.TeamBlock2)


        self.horizontalLayout_3.addLayout(self.BlockForTeamSet2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.load_teams = QPushButton(self.verticalFrame)
        self.load_teams.setObjectName(u"load_teams")

        self.horizontalLayout_6.addWidget(self.load_teams)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = QPushButton(self.verticalFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.select_teams_file = QPushButton(self.verticalFrame)
        self.select_teams_file.setObjectName(u"select_teams_file")

        self.horizontalLayout_6.addWidget(self.select_teams_file)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.load_pid = QPushButton(self.verticalFrame)
        self.load_pid.setObjectName(u"load_pid")

        self.horizontalLayout_6.addWidget(self.load_pid)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.SetTeams)
        self.Manual = QWidget()
        self.Manual.setObjectName(u"Manual")
        self.gridFrame = QFrame(self.Manual)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(0, 0, 637, 429))
        self.gridLayout_3 = QGridLayout(self.gridFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ManualIcons = QFrame(self.gridFrame)
        self.ManualIcons.setObjectName(u"ManualIcons")
        self.verticalLayout_6 = QVBoxLayout(self.ManualIcons)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalFrame = QFrame(self.ManualIcons)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 20))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.Title = QLabel(self.horizontalFrame)
        self.Title.setObjectName(u"Title")

        self.horizontalLayout_9.addWidget(self.Title)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_6.addWidget(self.horizontalFrame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.TeamB = QLabel(self.ManualIcons)
        self.TeamB.setObjectName(u"TeamB")
        self.TeamB.setMinimumSize(QSize(125, 16))

        self.gridLayout.addWidget(self.TeamB, 0, 1, 1, 1)

        self.TeamB_box = QComboBox(self.ManualIcons)
        self.TeamB_box.setObjectName(u"TeamB_box")

        self.gridLayout.addWidget(self.TeamB_box, 1, 1, 1, 1)

        self.TeamA = QLabel(self.ManualIcons)
        self.TeamA.setObjectName(u"TeamA")
        self.TeamA.setMinimumSize(QSize(125, 16))

        self.gridLayout.addWidget(self.TeamA, 0, 0, 1, 1)

        self.TeamA_box = QComboBox(self.ManualIcons)
        self.TeamA_box.setObjectName(u"TeamA_box")

        self.gridLayout.addWidget(self.TeamA_box, 1, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.TeamC_box = QComboBox(self.ManualIcons)
        self.TeamC_box.setObjectName(u"TeamC_box")

        self.gridLayout_2.addWidget(self.TeamC_box, 1, 0, 1, 1)

        self.TeamD_box = QComboBox(self.ManualIcons)
        self.TeamD_box.setObjectName(u"TeamD_box")

        self.gridLayout_2.addWidget(self.TeamD_box, 1, 1, 1, 1)

        self.TeamD = QLabel(self.ManualIcons)
        self.TeamD.setObjectName(u"TeamD")
        self.TeamD.setMinimumSize(QSize(125, 16))

        self.gridLayout_2.addWidget(self.TeamD, 0, 1, 1, 1)

        self.TeamC = QLabel(self.ManualIcons)
        self.TeamC.setObjectName(u"TeamC")
        self.TeamC.setMinimumSize(QSize(125, 16))

        self.gridLayout_2.addWidget(self.TeamC, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Intensity = QComboBox(self.ManualIcons)
        self.Intensity.setObjectName(u"Intensity")

        self.horizontalLayout_11.addWidget(self.Intensity)

        self.MessageTeam = QPushButton(self.ManualIcons)
        self.MessageTeam.setObjectName(u"MessageTeam")

        self.horizontalLayout_11.addWidget(self.MessageTeam)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.ManualIcons)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Manual)
        self.Automatic = QWidget()
        self.Automatic.setObjectName(u"Automatic")
        self.formLayoutWidget = QWidget(self.Automatic)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(230, 140, 239, 80))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.pushButton)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.stackedWidget.addWidget(self.Automatic)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Main_Menus)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 781, 72))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"#frame{\n"
"border-radius: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalFrame_21 = QFrame(self.frame)
        self.horizontalFrame_21.setObjectName(u"horizontalFrame_21")
        self.horizontalFrame_21.setGeometry(QRect(300, 0, 231, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame_21)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.horizontalFrame_21)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 25, 102, 30))
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
        self.SwitchPager.setText(QCoreApplication.translate("MainWindow", u"Set Pagers", None))
        self.SwitchManual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.SwitchAuto.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.label_2.setText("")
        self.TeamTitleLable.setText(QCoreApplication.translate("MainWindow", u"Enter Team Info", None))
        self.PagerID1.setText(QCoreApplication.translate("MainWindow", u"Team Number", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pager ID", None))
        self.PagerID1_2.setText(QCoreApplication.translate("MainWindow", u"Team Number", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pager ID", None))
        self.load_teams.setText(QCoreApplication.translate("MainWindow", u"load teams", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Set teams", None))
        self.select_teams_file.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.load_pid.setText(QCoreApplication.translate("MainWindow", u"load Pid", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"MANUAL QUEUE", None))
        self.TeamB.setText(QCoreApplication.translate("MainWindow", u"Select Team B", None))
        self.TeamA.setText(QCoreApplication.translate("MainWindow", u"Select Team A", None))
        self.TeamD.setText(QCoreApplication.translate("MainWindow", u"Select Team D", None))
        self.TeamC.setText(QCoreApplication.translate("MainWindow", u"Select Team C", None))
        self.MessageTeam.setText(QCoreApplication.translate("MainWindow", u"Message Team", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start/Stop Automatic Mode", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status of Automatic mode", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pager Software", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

