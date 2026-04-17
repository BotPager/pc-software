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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 461)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 461))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setGeometry(QRect(0, 0, 950, 461))
        self.Content.setMaximumSize(QSize(1920, 16777215))
        self.Content.setFrameShape(QFrame.Shape.StyledPanel)
        self.Content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalFrame_2 = QFrame(self.Content)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setGeometry(QRect(0, 0, 950, 461))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy1)
        self.horizontalFrame_2.setMinimumSize(QSize(950, 0))
        self.horizontalFrame_2.setAutoFillBackground(False)
        self.horizontalFrame_2.setStyleSheet(u"#horizontalFrame_2{\n"
"	border-radius: 0px;\n"
"}")
        self.horizontalFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalFrame_2 = QFrame(self.horizontalFrame_2)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMinimumSize(QSize(0, 200))
        self.verticalFrame_2.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout.addWidget(self.verticalFrame_2)

        self.Main_Menus = QFrame(self.horizontalFrame_2)
        self.Main_Menus.setObjectName(u"Main_Menus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Main_Menus.sizePolicy().hasHeightForWidth())
        self.Main_Menus.setSizePolicy(sizePolicy2)
        self.Main_Menus.setMinimumSize(QSize(620, 400))
        self.Main_Menus.setMaximumSize(QSize(640, 500))
        self.Main_Menus.setFrameShape(QFrame.Shape.StyledPanel)
        self.Main_Menus.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.Main_Menus)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SwitchPager = QPushButton(self.Main_Menus)
        self.SwitchPager.setObjectName(u"SwitchPager")
        self.SwitchPager.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_7.addWidget(self.SwitchPager)

        self.SwitchPair = QPushButton(self.Main_Menus)
        self.SwitchPair.setObjectName(u"SwitchPair")
        self.SwitchPair.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_7.addWidget(self.SwitchPair)

        self.SwitchManual = QPushButton(self.Main_Menus)
        self.SwitchManual.setObjectName(u"SwitchManual")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(20)
        sizePolicy3.setHeightForWidth(self.SwitchManual.sizePolicy().hasHeightForWidth())
        self.SwitchManual.setSizePolicy(sizePolicy3)
        self.SwitchManual.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_7.addWidget(self.SwitchManual)

        self.SwitchAuto = QPushButton(self.Main_Menus)
        self.SwitchAuto.setObjectName(u"SwitchAuto")
        self.SwitchAuto.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_7.addWidget(self.SwitchAuto)

        self.pushButton_3 = QPushButton(self.Main_Menus)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_7.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.stackedWidget = QStackedWidget(self.Main_Menus)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setMinimumSize(QSize(600, 260))
        self.stackedWidget.setAutoFillBackground(True)
        self.SetTeams = QWidget()
        self.SetTeams.setObjectName(u"SetTeams")
        self.SetTeams.setMinimumSize(QSize(616, 383))
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
        self.clear_all = QPushButton(self.verticalFrame)
        self.clear_all.setObjectName(u"clear_all")

        self.horizontalLayout_6.addWidget(self.clear_all)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = QPushButton(self.verticalFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.select_teams_file = QPushButton(self.verticalFrame)
        self.select_teams_file.setObjectName(u"select_teams_file")

        self.horizontalLayout_6.addWidget(self.select_teams_file)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.SetTeams)
        self.Manual = QWidget()
        self.Manual.setObjectName(u"Manual")
        self.Manual.setMinimumSize(QSize(616, 383))
        self.gridFrame = QFrame(self.Manual)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(0, 0, 605, 385))
        self.gridFrame.setMinimumSize(QSize(605, 385))
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
        self.horizontalFrame = QFrame(self.ManualIcons)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 20))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

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
        self.TeamC = QLabel(self.ManualIcons)
        self.TeamC.setObjectName(u"TeamC")
        self.TeamC.setMinimumSize(QSize(125, 16))

        self.gridLayout_2.addWidget(self.TeamC, 0, 0, 1, 1)

        self.TeamD_box = QComboBox(self.ManualIcons)
        self.TeamD_box.setObjectName(u"TeamD_box")

        self.gridLayout_2.addWidget(self.TeamD_box, 1, 1, 1, 1)

        self.TeamD = QLabel(self.ManualIcons)
        self.TeamD.setObjectName(u"TeamD")
        self.TeamD.setMinimumSize(QSize(125, 16))

        self.gridLayout_2.addWidget(self.TeamD, 0, 1, 1, 1)

        self.TeamC_box = QComboBox(self.ManualIcons)
        self.TeamC_box.setObjectName(u"TeamC_box")

        self.gridLayout_2.addWidget(self.TeamC_box, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.MessageTeam = QPushButton(self.ManualIcons)
        self.MessageTeam.setObjectName(u"MessageTeam")
        self.MessageTeam.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_13.addWidget(self.MessageTeam)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.label_2 = QLabel(self.ManualIcons)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.TeamF_box = QComboBox(self.ManualIcons)
        self.TeamF_box.setObjectName(u"TeamF_box")
        self.TeamF_box.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_12.addWidget(self.TeamF_box)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)


        self.verticalLayout_6.addLayout(self.verticalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Message_single = QPushButton(self.ManualIcons)
        self.Message_single.setObjectName(u"Message_single")
        self.Message_single.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_11.addWidget(self.Message_single)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.label_6 = QLabel(self.ManualIcons)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Arena = QLabel(self.ManualIcons)
        self.Arena.setObjectName(u"Arena")
        self.Arena.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.Arena, 0, 1, 1, 1)

        self.Intensity = QComboBox(self.ManualIcons)
        self.Intensity.addItem("")
        self.Intensity.addItem("")
        self.Intensity.addItem("")
        self.Intensity.addItem("")
        self.Intensity.setObjectName(u"Intensity")
        self.Intensity.setMinimumContentsLength(0)

        self.gridLayout_6.addWidget(self.Intensity, 1, 0, 1, 1)

        self.label = QLabel(self.ManualIcons)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.Arena_select = QComboBox(self.ManualIcons)
        self.Arena_select.addItem("")
        self.Arena_select.addItem("")
        self.Arena_select.addItem("")
        self.Arena_select.addItem("")
        self.Arena_select.addItem("")
        self.Arena_select.addItem("")
        self.Arena_select.addItem("")
        self.Arena_select.addItem("")
        self.Arena_select.setObjectName(u"Arena_select")

        self.gridLayout_6.addWidget(self.Arena_select, 1, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_6)

        self.verticalFrame1 = QFrame(self.ManualIcons)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setMaximumSize(QSize(125, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.verticalLayout_6.addWidget(self.verticalFrame1)


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
        self.matchStateText = QTextEdit(self.Automatic)
        self.matchStateText.setObjectName(u"matchStateText")
        self.matchStateText.setGeometry(QRect(440, 160, 111, 91))
        self.matchStateText.setOverwriteMode(True)
        self.Title_2 = QLabel(self.Automatic)
        self.Title_2.setObjectName(u"Title_2")
        self.Title_2.setGeometry(QRect(250, 50, 111, 20))
        self.blueTeam2Text = QTextEdit(self.Automatic)
        self.blueTeam2Text.setObjectName(u"blueTeam2Text")
        self.blueTeam2Text.setGeometry(QRect(60, 280, 104, 31))
        self.blueTeam2Text.setOverwriteMode(True)
        self.redTeam1Text = QTextEdit(self.Automatic)
        self.redTeam1Text.setObjectName(u"redTeam1Text")
        self.redTeam1Text.setGeometry(QRect(60, 100, 104, 31))
        self.redTeam1Text.setOverwriteMode(True)
        self.redTeam2Text = QTextEdit(self.Automatic)
        self.redTeam2Text.setObjectName(u"redTeam2Text")
        self.redTeam2Text.setGeometry(QRect(60, 160, 104, 31))
        self.redTeam2Text.setOverwriteMode(True)
        self.blueTeam1Text = QTextEdit(self.Automatic)
        self.blueTeam1Text.setObjectName(u"blueTeam1Text")
        self.blueTeam1Text.setGeometry(QRect(60, 220, 104, 31))
        self.blueTeam1Text.setOverwriteMode(True)
        self.Title_3 = QLabel(self.Automatic)
        self.Title_3.setObjectName(u"Title_3")
        self.Title_3.setGeometry(QRect(60, 80, 111, 20))
        self.Title_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Title_4 = QLabel(self.Automatic)
        self.Title_4.setObjectName(u"Title_4")
        self.Title_4.setGeometry(QRect(60, 140, 111, 20))
        self.Title_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Title_5 = QLabel(self.Automatic)
        self.Title_5.setObjectName(u"Title_5")
        self.Title_5.setGeometry(QRect(60, 200, 111, 20))
        self.Title_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Title_6 = QLabel(self.Automatic)
        self.Title_6.setObjectName(u"Title_6")
        self.Title_6.setGeometry(QRect(60, 260, 111, 20))
        self.Title_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Title_7 = QLabel(self.Automatic)
        self.Title_7.setObjectName(u"Title_7")
        self.Title_7.setGeometry(QRect(440, 140, 111, 20))
        self.Title_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.Automatic)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 160, 223, 91))
        self.label_3 = QLabel(self.Automatic)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 133, 223, 21))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fieldNumText = QTextEdit(self.Automatic)
        self.fieldNumText.setObjectName(u"fieldNumText")
        self.fieldNumText.setGeometry(QRect(440, 280, 110, 31))
        self.fieldNumText.setOverwriteMode(True)
        self.Title_8 = QLabel(self.Automatic)
        self.Title_8.setObjectName(u"Title_8")
        self.Title_8.setGeometry(QRect(440, 260, 111, 20))
        self.Title_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Title_9 = QLabel(self.Automatic)
        self.Title_9.setObjectName(u"Title_9")
        self.Title_9.setGeometry(QRect(440, 80, 111, 20))
        self.Title_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.qualNumText = QTextEdit(self.Automatic)
        self.qualNumText.setObjectName(u"qualNumText")
        self.qualNumText.setGeometry(QRect(440, 100, 110, 31))
        self.qualNumText.setOverwriteMode(True)
        self.stackedWidget.addWidget(self.Automatic)
        self.Provision = QWidget()
        self.Provision.setObjectName(u"Provision")
        self.Provision.setMinimumSize(QSize(616, 383))
        self.horizontalFrame1 = QFrame(self.Provision)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalFrame1.setGeometry(QRect(0, 0, 616, 383))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.verticalFrame_3 = QFrame(self.horizontalFrame1)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalLayout_7 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.Provision_button = QPushButton(self.verticalFrame_3)
        self.Provision_button.setObjectName(u"Provision_button")

        self.verticalLayout_7.addWidget(self.Provision_button)

        self.Pairbutton = QTextBrowser(self.verticalFrame_3)
        self.Pairbutton.setObjectName(u"Pairbutton")

        self.verticalLayout_7.addWidget(self.Pairbutton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.horizontalLayout_10.addWidget(self.verticalFrame_3)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.stackedWidget.addWidget(self.Provision)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Main_Menus)

        self.verticalFrame2 = QFrame(self.horizontalFrame_2)
        self.verticalFrame2.setObjectName(u"verticalFrame2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridFrame_2 = QFrame(self.verticalFrame2)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridLayout_5 = QGridLayout(self.gridFrame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Teams_set_indicator = QLabel(self.gridFrame_2)
        self.Teams_set_indicator.setObjectName(u"Teams_set_indicator")

        self.gridLayout_5.addWidget(self.Teams_set_indicator, 2, 1, 1, 1)

        self.Automatic_indicator = QLabel(self.gridFrame_2)
        self.Automatic_indicator.setObjectName(u"Automatic_indicator")

        self.gridLayout_5.addWidget(self.Automatic_indicator, 1, 1, 1, 1)

        self.Pager_conn_indicator = QLabel(self.gridFrame_2)
        self.Pager_conn_indicator.setObjectName(u"Pager_conn_indicator")

        self.gridLayout_5.addWidget(self.Pager_conn_indicator, 0, 1, 1, 1)

        self.Automatic_txt = QLabel(self.gridFrame_2)
        self.Automatic_txt.setObjectName(u"Automatic_txt")

        self.gridLayout_5.addWidget(self.Automatic_txt, 1, 0, 1, 1)

        self.Connection_txt = QLabel(self.gridFrame_2)
        self.Connection_txt.setObjectName(u"Connection_txt")

        self.gridLayout_5.addWidget(self.Connection_txt, 0, 0, 1, 1)

        self.Teams_txt = QLabel(self.gridFrame_2)
        self.Teams_txt.setObjectName(u"Teams_txt")

        self.gridLayout_5.addWidget(self.Teams_txt, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.gridFrame_2)

        self.Errorbox = QTextEdit(self.verticalFrame2)
        self.Errorbox.setObjectName(u"Errorbox")
        self.Errorbox.setMaximumSize(QSize(225, 16777215))

        self.verticalLayout_3.addWidget(self.Errorbox)


        self.horizontalLayout.addWidget(self.verticalFrame2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.Intensity.setCurrentIndex(3)
        self.Arena_select.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SwitchPager.setText(QCoreApplication.translate("MainWindow", u"Set Pagers", None))
        self.SwitchPair.setText(QCoreApplication.translate("MainWindow", u"Pairing", None))
        self.SwitchManual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.SwitchAuto.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.TeamTitleLable.setText(QCoreApplication.translate("MainWindow", u"Enter Team Info", None))
        self.PagerID1.setText(QCoreApplication.translate("MainWindow", u"Team Number", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pager ID", None))
        self.PagerID1_2.setText(QCoreApplication.translate("MainWindow", u"Team Number", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pager ID", None))
        self.clear_all.setText(QCoreApplication.translate("MainWindow", u"Clear all", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Set teams", None))
        self.select_teams_file.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.TeamB.setText(QCoreApplication.translate("MainWindow", u"Red 2", None))
        self.TeamA.setText(QCoreApplication.translate("MainWindow", u"Red 1", None))
        self.TeamC.setText(QCoreApplication.translate("MainWindow", u"Blue 1", None))
        self.TeamD.setText(QCoreApplication.translate("MainWindow", u"Blue 2", None))
        self.MessageTeam.setText(QCoreApplication.translate("MainWindow", u"Message Teams", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Single Team", None))
        self.Message_single.setText(QCoreApplication.translate("MainWindow", u"Message Team", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.Arena.setText(QCoreApplication.translate("MainWindow", u"Arena", None))
        self.Intensity.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.Intensity.setItemText(1, QCoreApplication.translate("MainWindow", u"Page low", None))
        self.Intensity.setItemText(2, QCoreApplication.translate("MainWindow", u"Page high", None))
        self.Intensity.setItemText(3, QCoreApplication.translate("MainWindow", u"Parts", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Message Type", None))
        self.Arena_select.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.Arena_select.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.Arena_select.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.Arena_select.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.Arena_select.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.Arena_select.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.Arena_select.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.Arena_select.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.matchStateText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.Title_2.setText(QCoreApplication.translate("MainWindow", u"AUTOMATIC QUEUE", None))
        self.blueTeam2Text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.redTeam1Text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.redTeam2Text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.blueTeam1Text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.Title_3.setText(QCoreApplication.translate("MainWindow", u"Red Team 1:", None))
        self.Title_4.setText(QCoreApplication.translate("MainWindow", u"Red Team 2:", None))
        self.Title_5.setText(QCoreApplication.translate("MainWindow", u"Blue Team 1:", None))
        self.Title_6.setText(QCoreApplication.translate("MainWindow", u"Blue Team 2:", None))
        self.Title_7.setText(QCoreApplication.translate("MainWindow", u"Match State", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Automatic Mode Toggle", None))
        self.fieldNumText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.Title_8.setText(QCoreApplication.translate("MainWindow", u"Field #", None))
        self.Title_9.setText(QCoreApplication.translate("MainWindow", u"Qualification #", None))
        self.qualNumText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.Provision_button.setText(QCoreApplication.translate("MainWindow", u"Provision Pager", None))
        self.Teams_set_indicator.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Automatic_indicator.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Pager_conn_indicator.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Automatic_txt.setText(QCoreApplication.translate("MainWindow", u"Automatic on:", None))
        self.Connection_txt.setText(QCoreApplication.translate("MainWindow", u"Pager Connection:", None))
        self.Teams_txt.setText(QCoreApplication.translate("MainWindow", u"Teams Set:", None))
    # retranslateUi

