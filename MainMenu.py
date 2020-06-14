# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import OpenCvManager
import StudentDataBaseProcessor
from RegisterMenu import Ui_RegisterWindow
import DataBase
from ShowListMenu import Ui_ShowListWindow


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        #standart settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 279)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setText("---Вікно адміністратора---")
        #self.titleLabel.setText("---Вікно працівника---")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.titleLabel)

        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)

        spacerItem = QtWidgets.QSpacerItem(5, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.horizontalLayoutForMonitoring = QtWidgets.QHBoxLayout()
        self.enterCheckBox = QtWidgets.QCheckBox("Вхід у приміщення")
        self.exitCheckBox = QtWidgets.QCheckBox("Вихід з приміщення")
        self.monitoringButton = QtWidgets.QPushButton(self.centralwidget)
        self.monitoringButton.setObjectName("monitoringButton")
        self.horizontalLayoutForMonitoring.addWidget(self.enterCheckBox)
        self.horizontalLayoutForMonitoring.addWidget(self.exitCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayoutForMonitoring)

        self.verticalLayout.addWidget(self.monitoringButton)

        self.verticalLayout.addItem(spacerItem)

        self.listButton = QtWidgets.QPushButton(self.centralwidget)
        self.listButton.setObjectName("listButton")
        self.verticalLayout.addWidget(self.listButton)
        #self.cameraOnlineLabel = QtWidgets.QLabel(self.centralwidget)
        #self.cameraOnlineLabel.setObjectName("cameraOnlineLabel")
        #self.verticalLayout.addWidget(self.cameraOnlineLabel)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.video = QtWidgets.QWidget(self.centralwidget)
        self.video.setObjectName("video")
        #self.verticalLayout_2.addWidget(self.video)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # connect to slots
        #self.enterCheckBox.toggled()

        self.monitoringButton.clicked.connect(self.StartMonitoring)
        self.registerButton.clicked.connect(self.OpenRegisterStudentWindow)
        self.listButton.clicked.connect(self.OpenResultListWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # create opencv stuff
        self.OpenCvManager = OpenCvManager.OpenCvManager()

        # create db stuff
        self.DBManager = DataBase.DataBase()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registerButton.setText(_translate("MainWindow", "Занесення особистих даних"))
        self.monitoringButton.setText(_translate("MainWindow", "Почати моніторинг"))
        self.listButton.setText(_translate("MainWindow", "Вивести результати"))
        #self.cameraOnlineLabel.setText(_translate("MainWindow", "Camera online:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    # TODO add some code
    def StartMonitoring(self):
        isEnterMode = self.enterCheckBox.isChecked()
        self.OpenCvManager.StartMonitoring(self.DBManager, isEnterMode)

    def OpenRegisterStudentWindow(self):
        self.registerWindow = QtWidgets.QMainWindow()
        self.registerWindowUI = Ui_RegisterWindow()
        self.registerWindowUI.setupUi(self.registerWindow, self.OpenCvManager, self.DBManager)
        self.registerWindow.show()
        #MainWindow.setDisabled(True)

    def OpenResultListWindow(self):
        self.listResultWindow = QtWidgets.QMainWindow()
        self.listResultWindowUI = Ui_ShowListWindow()
        self.listResultWindowUI.setupUi(self.listResultWindow, self.DBManager)
        self.listResultWindow.show()


class RegisterWindow():
    def __init__(self):
        super.__init__()

    #def initRegisterUI(self):



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

