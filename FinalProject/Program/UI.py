
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import sys
import api
import apiCalls
import base64

#GLOBAL LOGIN PARAM
Login = False
globalPhoto = None
globalSysID = None
api_instance = None

def getApi():
    return api_instance

def setApi(instance):
    global api_instance
    api_instance = instance


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #FFFFFF")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-10, 50, 1281, 720))
        self.stackedWidget.setMinimumSize(QSize(1280, 720))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: #FFFFFF")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        #username input
        self.usernameInput = QLineEdit(self.loginPage)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setGeometry(QRect(520, 230, 291, 31))
        self.usernameInput.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        
        #Password input
        self.passwordInput = QLineEdit(self.loginPage)
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(520, 290, 291, 31))
        self.passwordInput.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        
        
        self.usernameLabel = QLabel(self.loginPage)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(440, 230, 71, 31))
        self.usernameLabel.setStyleSheet(u"color: #000000")
        self.passwordLabel = QLabel(self.loginPage)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(440, 290, 71, 31))
        self.passwordLabel.setStyleSheet(u"color: #000000")
        #Login button
        self.loginButton = QPushButton(self.loginPage)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(600, 350, 121, 41))
        self.loginButton.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.loginButton.clicked.connect(self.loginMethod)
        
        
        
        #Home page
        self.stackedWidget.addWidget(self.loginPage)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.frame2 = QLabel(self.Home)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(340, 20, 301, 301))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setStyleSheet(u"background-color: #D9D9D9")
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.frame1 = QLabel(self.Home)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(20, 20, 301, 301))
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setStyleSheet(u"background-color: lightgray")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.leftWidget = QStackedWidget(self.Home)
        self.leftWidget.setObjectName(u"leftWidget")
        self.leftWidget.setGeometry(QRect(20, 340, 1271, 311))
        self.leftNormal = QWidget()
        self.leftNormal.setObjectName(u"leftNormal")
        self.manualEmployeeButton = QPushButton(self.leftNormal)
        self.manualEmployeeButton.setObjectName(u"manualEmployeeButton")
        self.manualEmployeeButton.setGeometry(QRect(0, 0, 181, 41))
        self.manualEmployeeButton.setStyleSheet(u"background-color: #D9D9D9;\n""color: #000000")
        self.manualEmployeeButton.clicked.connect(self.showBottomEmployee)
        self.ManualGuestButton = QPushButton(self.leftNormal)
        self.ManualGuestButton.setObjectName(u"ManualGuestButton")
        self.ManualGuestButton.setGeometry(QRect(190, 0, 181, 41))
        self.ManualGuestButton.setStyleSheet(u"background-color: #D9D9D9;\n""color: #000000")
        self.ManualGuestButton.clicked.connect(self.showBottomGuest)
        self.leftWidget.addWidget(self.leftNormal)
        self.manualGuest = QWidget()
        self.manualGuest.setObjectName(u"manualGuest")
        self.hideGuestButton = QPushButton(self.manualGuest)
        self.hideGuestButton.setObjectName(u"hideGuestButton")
        self.hideGuestButton.setGeometry(QRect(0, 0, 141, 41))
        self.hideGuestButton.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.hideGuestButton.clicked.connect(self.showBottomNormal)
        self.guestComment_2 = QTextEdit(self.manualGuest)
        self.guestComment_2.setObjectName(u"guestComment_2")
        self.guestComment_2.setGeometry(QRect(150, 160, 341, 101))
        self.guestComment_2.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.guestComment = QLabel(self.manualGuest)
        self.guestComment.setObjectName(u"guestComment")
        self.guestComment.setGeometry(QRect(10, 160, 71, 21))
        self.guestComment.setStyleSheet(u"color: #000000")
        font = QFont()
        font.setPointSize(9)
        self.guestComment.setFont(font)
        self.guestFname = QLabel(self.manualGuest)
        self.guestFname.setObjectName(u"guestFname")
        self.guestFname.setGeometry(QRect(10, 60, 121, 31))
        self.guestFname.setFont(font)
        self.guestFname.setStyleSheet(u"color: #000000")
        self.verifyGuest = QPushButton(self.manualGuest)
        self.verifyGuest.setObjectName(u"verifyGuest")
        self.verifyGuest.setGeometry(QRect(0, 270, 181, 41))
        self.verifyGuest.setStyleSheet(u"background-color: #D9D9D9;\n""color: #000000")
        self.verifyGuest.clicked.connect(self.addGuestEntry)
        self.guestFname_2 = QLineEdit(self.manualGuest)
        self.guestFname_2.setObjectName(u"guestFname_2")
        self.guestFname_2.setGeometry(QRect(150, 60, 151, 31))
        self.guestFname_2.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.guestLname_2 = QLineEdit(self.manualGuest)
        self.guestLname_2.setObjectName(u"guestLname_2")
        self.guestLname_2.setGeometry(QRect(150, 110, 151, 31))
        self.guestLname_2.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.guestLname = QLabel(self.manualGuest)
        self.guestLname.setObjectName(u"guestLname")
        self.guestLname.setGeometry(QRect(10, 110, 121, 31))
        self.guestLname.setFont(font)
        self.guestLname.setStyleSheet(u"color: #000000")
        self.leftWidget.addWidget(self.manualGuest)
        self.bottomEmployee = QWidget()
        self.bottomEmployee.setObjectName(u"bottomEmployee")
        self.hideManual = QPushButton(self.bottomEmployee)
        self.hideManual.setObjectName(u"hideManual")
        self.hideManual.setGeometry(QRect(320, 0, 141, 41))
        self.hideManual.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.hideManual.clicked.connect(self.showBottomNormal)
        self.manualID = QLabel(self.bottomEmployee)
        self.manualID.setObjectName(u"manualID")
        self.manualID.setGeometry(QRect(320, 50, 81, 21))
        self.manualID.setFont(font)
        self.manualID.setStyleSheet(u"color: #000000")
        self.manualComment = QLabel(self.bottomEmployee)
        self.manualComment.setObjectName(u"manualComment")
        self.manualComment.setGeometry(QRect(320, 90, 121, 21))
        self.manualComment.setFont(font)
        self.manualComment.setStyleSheet(u"color: #000000")
        self.manualComment_2 = QTextEdit(self.bottomEmployee)
        self.manualComment_2.setObjectName(u"manualComment_2")
        self.manualComment_2.setGeometry(QRect(420, 90, 341, 81))
        self.manualComment_2.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.manualID_2 = QSpinBox(self.bottomEmployee)
        self.manualID_2.setObjectName(u"manualID_2")
        self.manualID_2.setGeometry(QRect(420, 51, 61, 31))
        font1 = QFont()
        font1.setPointSize(13)
        self.manualID_2.setFont(font1)
        self.manualID_2.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.manualGetPhotoButton = QPushButton(self.bottomEmployee)
        self.manualGetPhotoButton.setObjectName(u"manualGetPhotoButton")
        self.manualGetPhotoButton.setGeometry(QRect(490, 50, 71, 31))
        self.manualGetPhotoButton.setStyleSheet(u"background-color: #D9D9D9;\n""color: #000000")
        self.manualGetPhotoButton.clicked.connect(self.manaulPhotoGet)
        self.manualPhoto = QLabel(self.bottomEmployee)
        self.manualPhoto.setObjectName(u"manualPhoto")
        self.manualPhoto.setGeometry(QRect(0, 0, 301, 301))
        sizePolicy.setHeightForWidth(self.manualPhoto.sizePolicy().hasHeightForWidth())
        self.manualPhoto.setSizePolicy(sizePolicy)
        self.manualPhoto.setStyleSheet(u"background-color: #D9D9D9")
        self.manualPhoto.setFrameShape(QFrame.StyledPanel)
        self.manualPhoto.setFrameShadow(QFrame.Raised)
        self.manualVerify = QPushButton(self.bottomEmployee)
        self.manualVerify.setObjectName(u"manualVerify")
        self.manualVerify.setGeometry(QRect(420, 200, 141, 41))
        self.manualVerify.setStyleSheet(u"background-color: #D9D9D9;\n""color: #000000")
        self.manualVerify.clicked.connect(self.addEmployeeEntry)
        self.leftWidget.addWidget(self.bottomEmployee)
        self.personInfo1 = QTextBrowser(self.Home)
        self.personInfo1.setObjectName(u"personInfo1")
        self.personInfo1.setGeometry(QRect(650, 210, 631, 111))
        sizePolicy.setHeightForWidth(self.personInfo1.sizePolicy().hasHeightForWidth())
        self.personInfo1.setSizePolicy(sizePolicy)
        self.personInfo1.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.stackedWidget.addWidget(self.Home)
        self.frame2.raise_()
        self.leftWidget.raise_()
        self.frame1.raise_()
        self.personInfo1.raise_()
        
        
        #self.findEmployeesButton.clicked.connect(self.GetEmployee)
        #database page
        self.Database = QWidget()
        self.Database.setObjectName(u"Database")
        self.IDBox = QSpinBox(self.Database)
        self.IDBox.setObjectName(u"IDBox")
        self.IDBox.setGeometry(QRect(930, 20, 91, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.IDBox.setFont(font2)
        self.IDBox.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.IDBox.setMinimum(1)
        self.IDBox.setMaximum(999)
        self.IDBox.setValue(1)
        self.IDLabel = QLabel(self.Database)
        self.IDLabel.setObjectName(u"IDLabel")
        self.IDLabel.setGeometry(QRect(830, 20, 91, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.IDLabel.setFont(font3)
        self.IDLabel.setStyleSheet(u"color: #000000")
        self.findEmployeesButton = QPushButton(self.Database)
        self.findEmployeesButton.setObjectName(u"findEmployeesButton")
        self.findEmployeesButton.setGeometry(QRect(1040, 22, 91, 31))
        self.findEmployeesButton.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.findEmployeesButton.clicked.connect(self.GetEmployee)
        self.databaseText = QTextBrowser(self.Database)
        self.databaseText.setObjectName(u"databaseText")
        self.databaseText.setGeometry(QRect(20, 80, 651, 551))
        self.databaseText.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.employeeText = QTextBrowser(self.Database)
        self.employeeText.setObjectName(u"employeeText")
        self.employeeText.setGeometry(QRect(830, 80, 441, 91))
        self.employeeText.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.Label_1 = QLabel(self.Database)
        self.Label_1.setObjectName(u"Label_1")
        self.Label_1.setGeometry(QRect(110, 60, 501, 16))
        self.Label_1.setStyleSheet(u"color: #000000")
        self.label_2 = QLabel(self.Database)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(830, 60, 141, 20))
        self.label_2.setStyleSheet(u"color: #000000")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.photoFrame = QLabel(self.Database)
        self.photoFrame.setObjectName(u"photoFrame")
        self.photoFrame.setGeometry(QRect(830, 210, 441, 421))
        self.photoFrame.setStyleSheet(u"background-color: #D9D9D9")
        self.photoFrame.setFrameShape(QFrame.StyledPanel)
        self.photoFrame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.Database)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(830, 190, 111, 20))
        self.label_3.setStyleSheet(u"color: #000000")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.findEmployeesButton_2 = QPushButton(self.Database)
        self.findEmployeesButton_2.setObjectName(u"findEmployeesButton_2")
        self.findEmployeesButton_2.setGeometry(QRect(580, 20, 91, 31))
        self.findEmployeesButton_2.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.findEmployeesButton_2.clicked.connect(self.DisplayEntries)
        self.numberOfEntries = QSpinBox(self.Database)
        self.numberOfEntries.setObjectName(u"numberOfEntries")
        self.numberOfEntries.setGeometry(QRect(200, 20, 71, 31))
        self.numberOfEntries.setFont(font2)
        self.numberOfEntries.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.numberOfEntries.setMinimum(1)
        self.numberOfEntries.setMaximum(100)
        self.numberOfEntries.setValue(10)
        self.Label_2 = QLabel(self.Database)
        self.Label_2.setObjectName(u"Label_2")
        self.Label_2.setGeometry(QRect(20, 20, 171, 31))
        font4 = QFont()
        font4.setPointSize(7)
        self.Label_2.setFont(font4)
        self.Label_2.setStyleSheet(u"color: #000000")
        self.numberOfEntries_2 = QSpinBox(self.Database)
        self.numberOfEntries_2.setObjectName(u"numberOfEntries_2")
        self.numberOfEntries_2.setGeometry(QRect(500, 20, 71, 31))
        self.numberOfEntries_2.setFont(font2)
        self.numberOfEntries_2.setStyleSheet(u"background-color: #D9D9D9; color: #000000")
        self.numberOfEntries_2.setMinimum(-2)
        self.numberOfEntries_2.setMaximum(100)
        self.numberOfEntries_2.setValue(0)
        self.Label_3 = QLabel(self.Database)
        self.Label_3.setObjectName(u"Label_3")
        self.Label_3.setGeometry(QRect(280, 20, 201, 31))
        self.Label_3.setFont(font4)
        self.Label_3.setStyleSheet(u"color: #000000")
        self.Label_3.setTextFormat(Qt.AutoText)
        self.Label_3.setWordWrap(True)
        self.stackedWidget.addWidget(self.Database)
        
        
        
        ############## ADD USER PAGE
        self.addUserPage = QWidget()
        self.addUserPage.setObjectName(u"addUserPage")
        
        self.NewEmployeePhoto = QLabel(self.addUserPage)
        self.NewEmployeePhoto.setObjectName(u"NewEmployeePhoto")
        self.NewEmployeePhoto.setGeometry(QRect(400, 120, 521, 491))
        self.NewEmployeePhoto.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.NewEmployeePhoto.setFrameShape(QFrame.StyledPanel)
        self.NewEmployeePhoto.setFrameShadow(QFrame.Raised)
        self.takePhotoButton = QPushButton(self.addUserPage)
        self.takePhotoButton.setObjectName(u"takePhotoButton")
        self.takePhotoButton.setGeometry(QRect(400, 70, 131, 41))
        self.takePhotoButton.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.takePhotoButton.clicked.connect(self.clearPhoto)
        
        
        self.addEmployeeButton = QPushButton(self.addUserPage)
        self.addEmployeeButton.setObjectName(u"addEmployeeButton")
        self.addEmployeeButton.setGeometry(QRect(210, 500, 161, 41))
        self.addEmployeeButton.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.addEmployeeButton.clicked.connect(self.addEmployee)
        self.fnameLine = QLineEdit(self.addUserPage)
        self.fnameLine.setObjectName(u"fnameLine")
        self.fnameLine.setGeometry(QRect(170, 140, 201, 31))
        self.fnameLine.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.lnameLine = QLineEdit(self.addUserPage)
        self.lnameLine.setObjectName(u"lnameLine")
        self.lnameLine.setGeometry(QRect(170, 200, 201, 31))
        self.lnameLine.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.dob = QDateEdit(self.addUserPage)
        self.dob.setObjectName(u"dob")
        self.dob.setGeometry(QRect(170, 260, 201, 31))
        self.dob.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.label = QLabel(self.addUserPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 351, 31))
        self.label.setStyleSheet(u"color: #000000")
        font3 = QFont()
        font3.setPointSize(11)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.addUserPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 140, 71, 31))
        self.label_4.setStyleSheet(u"color: #000000")
        self.label_5 = QLabel(self.addUserPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 200, 71, 31))
        self.label_5.setStyleSheet(u"color: #000000")
        self.label_6 = QLabel(self.addUserPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 260, 71, 31))
        self.label_6.setStyleSheet(u"color: #000000")
        self.label_7 = QLabel(self.addUserPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 320, 351, 31))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: #000000")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.idLine = QLineEdit(self.addUserPage)
        self.idLine.setObjectName(u"idLine")
        self.idLine.setGeometry(QRect(170, 380, 201, 31))
        self.idLine.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.passwordLine = QLineEdit(self.addUserPage)
        self.passwordLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setGeometry(QRect(170, 440, 201, 31))
        self.passwordLine.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.label_8 = QLabel(self.addUserPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 440, 71, 31))
        self.label_8.setStyleSheet(u"color: #000000")
        self.label_9 = QLabel(self.addUserPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(90, 380, 71, 31))
        self.label_9.setStyleSheet(u"color: #000000")
        self.label_10 = QLabel(self.addUserPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(540, 70, 381, 41))
        font4 = QFont()
        font4.setPointSize(8)
        self.label_10.setFont(font4)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setStyleSheet(u"color: #000000")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.CreatedEmployee = QTextBrowser(self.addUserPage)
        self.CreatedEmployee.setObjectName(u"CreatedEmployee")
        self.CreatedEmployee.setGeometry(QRect(930, 120, 351, 491))
        self.CreatedEmployee.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.label_11 = QLabel(self.addUserPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(980, 70, 271, 41))
        self.label_11.setFont(font4)
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setStyleSheet(u"color: #000000")
        self.label_11.setAlignment(Qt.AlignCenter)
        
        
        self.stackedWidget.addWidget(self.addUserPage)
        #################TOP BUTTONS
        
        #Home Button
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(10, 10, 131, 51))
        self.homeButton.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.homeButton.clicked.connect(self.showHome)
        
        #Database Button
        self.databaseButton = QPushButton(self.centralwidget)
        self.databaseButton.setObjectName(u"databaseButton")
        self.databaseButton.setGeometry(QRect(150, 10, 131, 51))
        self.databaseButton.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.databaseButton.clicked.connect(self.showDatabase)
        
        
        #Text window
        self.errorTextDisplay = QTextBrowser(self.centralwidget)
        self.errorTextDisplay.setObjectName(u"errorTextDisplay")
        self.errorTextDisplay.setGeometry(QRect(580, 10, 691, 51))
        self.errorTextDisplay.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.addUserButton = QPushButton(self.centralwidget)
        self.addUserButton.setObjectName(u"addUserButton")
        self.addUserButton.setGeometry(QRect(290, 10, 131, 51))
        self.addUserButton.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.addUserButton.clicked.connect(self.showAddUser)
        
        
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(430, 10, 131, 51))
        self.logoutButton.setStyleSheet(u"background-color: #D9D9D9;\n"
"color: #000000")
        self.logoutButton.clicked.connect(self.logoutMethod)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.manualEmployeeButton.setText(QCoreApplication.translate("MainWindow", u"Manual Employee Verification", None))
        self.ManualGuestButton.setText(QCoreApplication.translate("MainWindow", u"Manual Guest Entry", None))
        self.hideGuestButton.setText(QCoreApplication.translate("MainWindow", u"Hide Manual Controls", None))
        self.guestComment.setText(QCoreApplication.translate("MainWindow", u"Comment:", None))
        self.guestFname.setText(QCoreApplication.translate("MainWindow", u"Guest First Name:", None))
        self.verifyGuest.setText(QCoreApplication.translate("MainWindow", u"Allow Entry (and open gate)", None))
        self.guestLname.setText(QCoreApplication.translate("MainWindow", u"Guest Last Name:", None))
        self.hideManual.setText(QCoreApplication.translate("MainWindow", u"Hide Manual Controls", None))
        self.manualID.setText(QCoreApplication.translate("MainWindow", u"Employee ID:", None))
        self.manualComment.setText(QCoreApplication.translate("MainWindow", u"Comment:", None))
        self.manualGetPhotoButton.setText(QCoreApplication.translate("MainWindow", u"Get Photo", None))
        self.manualVerify.setText(QCoreApplication.translate("MainWindow", u"Verify (and open gate)", None))
        self.IDLabel.setText(QCoreApplication.translate("MainWindow", u"ID Number:", None))
        self.findEmployeesButton.setText(QCoreApplication.translate("MainWindow", u"Find Employee", None))
        self.Label_1.setText(QCoreApplication.translate("MainWindow", u"Log of entries (list is automatically updated when someone enters via gate:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Employee Information:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Employee Photo:", None))
        self.findEmployeesButton_2.setText(QCoreApplication.translate("MainWindow", u"Display Entries", None))
        self.Label_2.setText(QCoreApplication.translate("MainWindow", u"Amount of entries to be displayed", None))
        self.Label_3.setText(QCoreApplication.translate("MainWindow", u"Entries from specific employee or guest              (-1 for guests, 0 for all, or specific ID)", None))
        self.takePhotoButton.setText(QCoreApplication.translate("MainWindow", u"Clear photo", None))
        self.addEmployeeButton.setText(QCoreApplication.translate("MainWindow", u"Add Employee", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter employee details (ID is automatically set):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DoB:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Enter you login details:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Employee Photo (MUST BE CLEAR SHOT OF THEIR FACE (NO GLASSES!)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Created Employee:", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.databaseButton.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.addUserButton.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi


    #LOGIN PAGE
    def loginMethod(self):
        self.sendLoginRequest()
        global Login
        if Login == True:
            self.showHome()
            self.DisplayEntries()
        
    def logoutMethod(self):
        global Login
        if Login:
            Login = False
            self.display("Logged out!")
            self.showLogin()

    def sendLoginRequest(self):        
        try:
            global globalSysID
            id = int(self.usernameInput.text())
            globalSysID = int(self.usernameInput.text())
        except:
            self.display("ID incorrect (Must be a number)")
            
        password = self.passwordInput.text()
        api = getApi()
        result, error = api.SendLogin(id, password)

        if result == True:
            global Login
            Login = True
            self.display("")
        if result == False:
            text = "Login failed!"
            if error != None:
                text += f"  Error: {error}"
            self.display(text)
        
    #SHOW PAGES
    def showHome(self):
        global Login
        if Login:
            self.stackedWidget.setCurrentWidget(self.Home)

    def showBottomNormal(self):
        self.leftWidget.setCurrentWidget(self.leftNormal)
        
    def showBottomGuest(self):
        self.leftWidget.setCurrentWidget(self.manualGuest)
        
    def showBottomEmployee(self):
        self.leftWidget.setCurrentWidget(self.bottomEmployee)
      
    def showLogin(self):
        
        self.stackedWidget.setCurrentWidget(self.loginPage)
        
    def showDatabase(self):
        global Login
        if Login:
            self.stackedWidget.setCurrentWidget(self.Database)
    
    def showAddUser(self):
        global Login
        if Login:
            self.stackedWidget.setCurrentWidget(self.addUserPage)
        
    #HOME METHODS
    def display(self, text):
        self.errorTextDisplay.clear()
        self.errorTextDisplay.setText(text)    
        
    def middleDisplay(self, text1, text2, text3, text4, text5, text6):
        self.personInfo1.clear()
        if text2 is not None:
            text1 += text2
        if text3 is not None:
            text1 += text3
        if text4 is not None:
            text1 += text4
        if text5 is not None:
            text1 += text5
        if text6 is not None:
            text1 += text6
        self.personInfo1.setText(text1) 
    
    def displayImageLeft(self, img):
        
        if img is not None:
            try:
                _pixmap = QPixmap.fromImage(img)
                width = self.frame1.width()
                height = self.frame1.height()
                pixmap = _pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
                self.frame1.setPixmap(pixmap)
            except Exception as ex:
                print(f"Exception: {ex}")
        else:
            self.display("Failed to print left image")
            
    def displayImageRight(self, img):
        if img is None:
            self.frame2.clear()
            self.display("Failed to print right image")
        if img is not None:
            _img = QImage.fromData(img)
            try:
                _pixmap = QPixmap.fromImage(_img)
                width = self.frame2.width()
                height = self.frame2.height()
                pixmap = _pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
                self.frame2.setPixmap(pixmap)
            except Exception as ex:
                print(f"Exception: {ex}")
                self.display("Failed to print right image")
                self.frame2.clear()
        
    def ImgController(self, id, img):
        #self.middleDisplay(f"ID: {id}")
        try:
            _id = int(id)
        except Exception as ex:
            self.display(ex)
        _img = QImage.fromData(img)
        self.displayImageLeft(_img)
        try:
            calls.start(_id, "home")
        except Exception as ex:
            self.frame2.clear()
            self.display("Failed to print right image")
            
    def resultController(self, result):
        self.display(result)
        self.DisplayEntries()

    def addGuestEntry(self):
        id = -1
        guestFname = self.guestFname_2.text()
        if guestFname == "":
                self.display("First name is empty!")
                return
        guestLname = self.guestLname_2.text()
        if guestLname == "":
                self.display("Last name is empty!")
                return
        comment = self.guestComment_2.toPlainText()    
        if comment == "":
                self.display("Comment is empty!")
                return
        global globalSysID
        sysId = globalSysID
        name = ""
        name += f"Guest Name: {guestFname} {guestLname} \n Comment: "
        fullComment = name + comment
        api = getApi()
        try:
            api.OpenGate()
            api.AddEntry(id, fullComment, sysId)
            self.guestFname_2.clear()
            self.guestLname_2.clear()
            self.guestComment_2.clear()
        except Exception as ex:
            self.display(ex)
    
    def addEmployeeEntry(self):
        id = self.manualID_2.value()
        comment = self.manualComment_2.toPlainText()    
        if comment == "":
                self.display("Comment is empty!")
                return
        global globalSysID
        sysId = globalSysID
        api = getApi()
        try:
            api.OpenGate()
            api.AddEntry(id, comment, sysId)
            self.manualComment_2.clear()
            self.manualPhoto.clear()
        except Exception as ex:
            self.display(ex)
        
        
    def manaulPhotoGet(self):
        id = self.manualID_2.value()
        calls.start(id, "manual")
    
    def displayManualSettingsEmpPhoto(self, img):
        if img is None:
            self.manualPhoto.clear()
            self.display("Failed to print employee image, does employee have an image??")
        if img is not None:
            _img = QImage.fromData(img)
            try:
                _pixmap = QPixmap.fromImage(_img)
                width = self.manualPhoto.width()
                height = self.manualPhoto.height()
                pixmap = _pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
                self.manualPhoto.setPixmap(pixmap)
            except Exception as ex:
                print(f"Exception: {ex}")
                self.display("Failed to print employee image, does employee have an image???")
                self.manualPhoto.clear()
    
    #DATABASE PAGE METHODS
    def GetEmployee(self):
        self.photoFrame.clear()
        self.employeeText.clear()
        id = self.IDBox.value()
        calls.start(id, "database")
        
    def DisplayDatabaseDetails(self, text1, text2, text3, text4, text5, text6):
        self.employeeText.clear()
        if text2 is not None:
            text1 += text2
        if text3 is not None:
            text1 += text3
        if text4 is not None:
            text1 += text4
        if text5 is not None:
            text1 += text5
        if text6 is not None:
            text1 += text6
        self.employeeText.setText(text1) 
        
    def DisplayDatabaseImage(self, img):
        if img is None:
            self.photoFrame.clear()
            self.display("Failed to print employee image, does employee have an image??")
        if img is not None:
            _img = QImage.fromData(img)
            try:
                _pixmap = QPixmap.fromImage(_img)
                width = self.photoFrame.width()
                height = self.photoFrame.height()
                pixmap = _pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
                self.photoFrame.setPixmap(pixmap)
            except Exception as ex:
                print(f"Exception: {ex}")
                self.display("Failed to print employee image, does employee have an image???")
                self.photoFrame.clear()

    def DisplayEntries(self):
        num = self.numberOfEntries.value()
        id = self.numberOfEntries_2.value()
        api = getApi()
        entryList = []
        entryList = api.GetEntries(num, id)
        text = ""
        try:
            for entry in entryList:
                text += "------------------------------------------"
                if entry.manualEntry == "True":
                    text += str(f"\n MANUAL ENTRY!!! Details below")
                text += str(f"\n Entry number: {entry.entryNum}")
                if entry.employeeID != "-1":
                    text += str(f"\n Emloyee ID: {entry.employeeID}")
                text += str(f"\n Time of entry: {entry.entryTime}")
                if entry.employeeID == "-1":
                    text += str(f"\n {entry.comment}")
                    text += str(f"\n SysID: {entry.sysUserID}")
                if entry.employeeID != "-1" and entry.manualEntry == "True":
                    text += str(f"\n Comment: {entry.comment}")
                    text += str(f"\n SysID: {entry.sysUserID}")
                
                text += "\n"
            self.databaseText.setText(text)
        except Exception as ex:
            print(f"Display Entries error: {ex}")   
        
        
    #ADD USER METHODS
    def showEmpPhoto(self, img):
        global globalPhoto
        globalPhoto = img
        _img = QImage.fromData(img)
        if img is not None:
            try:
                _pixmap = QPixmap.fromImage(_img)
                width = self.NewEmployeePhoto.width()
                height = self.NewEmployeePhoto.height()
                pixmap = _pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
                self.NewEmployeePhoto.setPixmap(pixmap)
            except Exception as ex:
                print(f"Exception: {ex}")
        else:
            self.display("Failed to print left image")
    
    def addEmployee(self):
        try:
            try:
                _id = self.idLine.text()
                id = int(_id)
            except Exception as ex:
                self.display(f"Error: {ex}")
                
            password = self.passwordLine.text()
            
            global globalPhoto
            fname = self.fnameLine.text()
            if fname == "":
                self.display("First name is empty!")
                return
            lname = self.lnameLine.text()
            if lname == "":
                self.display("Last name is empty!")
                return
            dob = self.dob.date().toString("yyyy-MM-dd")
            photo = globalPhoto
            if photo == None:
                self.display("A photo must be attached to the employee")
                return
            photo_base64 = base64.b64encode(photo).decode('utf-8')

            
            try:
                id = int(self.idLine.text())
            except:
                self.display("ID incorrect (Must be a number)")
            
            password = self.passwordLine.text()

            api = getApi()
            response, error = api.AddEmployee(fname, lname, dob, photo_base64, id, password)
            
            print(f"Response: {response}")
            if response == True:
                self.fnameLine.clear()
                self.lnameLine.clear()
                
                default_date = QDate(2000, 1, 1)
                self.dob.setDate(default_date)
                
                globalPhoto = None
                self.display("Employee Added!")
            if response == False:
                self.display(f"Error: {error}")
            
        except Exception as ex:
            self.display(f"Error {ex}")

    def clearPhoto(self):
        global globalPhoto
        globalPhoto = None
        self.NewEmployeePhoto.clear()
        
        
    def DisplayAddUserDetails(self, text1, text2, text3, text4, text5, text6):#
        self.CreatedEmployee.clear()
        if text2 is not None:
            text1 += text2
        if text3 is not None:
            text1 += text3
        if text4 is not None:
            text1 += text4
        if text5 is not None:
            text1 += text5
        if text6 is not None:
            text1 += text6
        print(text1)
        self.CreatedEmployee.setText(text1)
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    # Create a plain QMainWindow
    main_window = QMainWindow()
    
    # Create the UI and set it up on the window
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    
    # Now you can access UI elements through ui
    # ui.pushButton.clicked.connect(some_function)
    
    # Show the window
    main_window.show()
    apiServer = api.Api()
    calls = apiCalls.apiCalls()
    setApi(calls)
    apiServer.image_received.connect(ui.ImgController)
    apiServer.result_received.connect(ui.resultController)
    apiServer.empImage_received.connect(ui.showEmpPhoto)
    calls.NotFoundSignal.connect(ui.display)
    calls.HomeImageSignal.connect(ui.displayImageRight)
    calls.ManualImageSignal.connect(ui.displayManualSettingsEmpPhoto)
    calls.HomeDetailsSignal.connect(ui.middleDisplay)
    calls.DatabaseDetailsSignal.connect(ui.DisplayDatabaseDetails)
    calls.DatabaseImageSignal.connect(ui.DisplayDatabaseImage)
    calls.AddUserDetailsSignal.connect(ui.DisplayAddUserDetails)
    
    
    
    apiServer.run()
    
    
    sys.exit(app.exec())
    
