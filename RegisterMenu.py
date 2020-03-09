# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from RegisterMenuManager import RegisterMenuManager
from Student import Student
import uuid


class Ui_RegisterWindow(object):
    def setupUi(self, MainWindow, OpenCvManager):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 492)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.firstNameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameLine.setObjectName("firstNameLine")
        self.horizontalLayout.addWidget(self.firstNameLine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.secondNameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.secondNameLine.setText("")
        self.secondNameLine.setObjectName("secondNameLine")
        self.horizontalLayout_2.addWidget(self.secondNameLine)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.instituteLine = QtWidgets.QLineEdit(self.centralwidget)
        self.instituteLine.setText("")
        self.instituteLine.setObjectName("instituteLine")
        self.horizontalLayout_3.addWidget(self.instituteLine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.professionLine = QtWidgets.QLineEdit(self.centralwidget)
        self.professionLine.setText("")
        self.professionLine.setObjectName("professionLine")
        self.horizontalLayout_4.addWidget(self.professionLine)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.groupLine = QtWidgets.QLineEdit(self.centralwidget)
        self.groupLine.setText("")
        self.groupLine.setObjectName("groupLine")
        self.horizontalLayout_5.addWidget(self.groupLine)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.edLevelComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.edLevelComboBox.setObjectName("edLevelComboBox")
        self.edLevelComboBox.addItem("")
        self.edLevelComboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.edLevelComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.ageLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ageLine.setText("")
        self.ageLine.setObjectName("ageLine")
        self.horizontalLayout_7.addWidget(self.ageLine)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.gpaLine = QtWidgets.QLineEdit(self.centralwidget)
        self.gpaLine.setText("")
        self.gpaLine.setObjectName("gpaLine")
        self.horizontalLayout_8.addWidget(self.gpaLine)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_2.addWidget(self.registerButton)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # connect to slots
        self.registerButton.clicked.connect(self.Register)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.OpenCvManager = OpenCvManager


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RegisterStudentWindow"))
        self.label.setText(_translate("MainWindow", "Please fill in registration form"))
        self.label_2.setText(_translate("MainWindow", "Enter first name"))
        self.firstNameLine.setPlaceholderText(_translate("MainWindow", "e.g. Sam"))
        self.label_3.setText(_translate("MainWindow", "Enter second name"))
        self.secondNameLine.setPlaceholderText(_translate("MainWindow", "e.g. Snow"))
        self.label_4.setText(_translate("MainWindow", "Enter institute name"))
        self.instituteLine.setPlaceholderText(_translate("MainWindow", "e.g. IKNI"))
        self.label_5.setText(_translate("MainWindow", "Enter type of profession"))
        self.professionLine.setPlaceholderText(_translate("MainWindow", "e.g. Computer scientist"))
        self.label_6.setText(_translate("MainWindow", "Enter group name"))
        self.groupLine.setPlaceholderText(_translate("MainWindow", "e.g. KN-412"))
        self.label_7.setText(_translate("MainWindow", "Choose educational level"))
        self.edLevelComboBox.setItemText(0, _translate("MainWindow", "Master"))
        self.edLevelComboBox.setItemText(1, _translate("MainWindow", "Bachelor"))
        self.label_8.setText(_translate("MainWindow", "Enter student age"))
        self.ageLine.setPlaceholderText(_translate("MainWindow", "e.g. 19"))
        self.label_9.setText(_translate("MainWindow", "Enter grade point average"))
        self.gpaLine.setPlaceholderText(_translate("MainWindow", "e.g. 82.5"))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.label_10.setText(_translate("MainWindow", "*after press Register button, it will be taken photo\nSmile:)"))

    def Register(self):
        student = Student(name=self.firstNameLine.text(),
                          surname=self.secondNameLine.text(),
                          pid=str(uuid.uuid4())[:4],
                          institute=self.instituteLine.text(),
                          profession=self.professionLine.text(),
                          group=self.groupLine.text(),
                          educationalLevel=self.edLevelComboBox.currentText(),
                          age=self.ageLine.text(),
                          gpa=self.gpaLine.text())
        # TODO maybe move next line to ctor
        manager = RegisterMenuManager(student)
        self.OpenCvManager.TakeAPhoto(manager.GetFolderPath())
        manager.RegisterInDataBase(self.OpenCvManager)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
