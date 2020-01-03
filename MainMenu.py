# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os

from RegisterMenu import Ui_RegisterWindow


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        #standart settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        self.monitoringButton = QtWidgets.QPushButton(self.centralwidget)
        self.monitoringButton.setObjectName("monitoringButton")
        self.verticalLayout.addWidget(self.monitoringButton)
        self.listButton = QtWidgets.QPushButton(self.centralwidget)
        self.listButton.setObjectName("listButton")
        self.verticalLayout.addWidget(self.listButton)
        self.cameraOnlineLabel = QtWidgets.QLabel(self.centralwidget)
        self.cameraOnlineLabel.setObjectName("cameraOnlineLabel")
        self.verticalLayout.addWidget(self.cameraOnlineLabel)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.video = QtWidgets.QWidget(self.centralwidget)
        self.video.setObjectName("video")
        self.verticalLayout_2.addWidget(self.video)
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
        self.monitoringButton.clicked.connect(self.StartMonitoring)
        self.registerButton.clicked.connect(self.OpenRegisterStudentWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registerButton.setText(_translate("MainWindow", "Register Student"))
        self.monitoringButton.setText(_translate("MainWindow", "Start monitoring"))
        self.listButton.setText(_translate("MainWindow", "Show lists of students"))
        self.cameraOnlineLabel.setText(_translate("MainWindow", "Camera online:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    # TODO add some code
    def StartMonitoring(self):
        cap = cv2.VideoCapture(0)
        while(True):
            ret, frame = cap.read()
            cv2.imshow('Video', frame)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    def OpenRegisterStudentWindow(self):
        self.registerWindow = QtWidgets.QMainWindow()
        self.registerWindowUI = Ui_RegisterWindow()
        self.registerWindowUI.setupUi(self.registerWindow)
        self.registerWindow.show()
        #MainWindow.setDisabled(True)



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

