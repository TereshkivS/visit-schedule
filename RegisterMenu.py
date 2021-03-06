# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newregisterwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from RegisterMenuManager import RegisterMenuManager
from Student import Student
import uuid
import DataBase

class Ui_RegisterWindow(object):
    def setupUi(self, MainWindow, OpenCvManager, DBManager):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 230)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setText("---Вікно реєстрації---")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.titleLabel)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Працівник")
        self.comboBox.addItem("Викладач")
        self.comboBox.addItem("Студент")
        self.verticalLayout_2.addWidget(self.comboBox)
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
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_2.addWidget(self.registerButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 17))
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

        self.comboBox.currentTextChanged.connect(self.ChangeUi)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.OpenCvManager = OpenCvManager
        self.manager = RegisterMenuManager()

        self.dataBaseManager = DBManager


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RegisterStudentWindow"))
        self.label.setText(_translate("MainWindow", "Будь ласка заповність форму реєстрації\nПоля із * є обов\'язковими"))
        self.label_2.setText(_translate("MainWindow", "* Ім\'я"))
        self.firstNameLine.setPlaceholderText(_translate("MainWindow", "Петро"))
        self.label_3.setText(_translate("MainWindow", "* Прізвище"))
        self.secondNameLine.setPlaceholderText(_translate("MainWindow", "Шухевич"))
        self.label_4.setText(_translate("MainWindow", "Інститут"))
        self.instituteLine.setPlaceholderText(_translate("MainWindow", "ІКНІ"))
        self.registerButton.setText(_translate("MainWindow", "Занести у базу даних"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    def Register(self):
        currentItem = self.comboBox.currentText()
        isSucessfullyRegistered = False
        if currentItem == "Викладач":
            while not isSucessfullyRegistered:
                isSucessfullyRegistered = self.ReadDataFromTeacherField()
                pass
        elif currentItem == "Працівник":
            while not isSucessfullyRegistered:
                isSucessfullyRegistered=self.ReadDataFromWorkerField()
                pass
        elif currentItem == "Студент":
            while not isSucessfullyRegistered:
                isSucessfullyRegistered=self.ReadDataFromStudentField()
                pass
        self.manager.CalculateFolerPath(self.firstNameLine.text(), self.secondNameLine.text())
        self.OpenCvManager.TakeAPhoto(self.manager.GetFolderPath())

        self.successedMakingPhotos = QtWidgets.QMessageBox()
        self.successedMakingPhotos.setIcon(QtWidgets.QMessageBox.Information)
        self.successedMakingPhotos.setText("Фото особи було зроблено успішно!")
        self.successedMakingPhotos.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.successedMakingPhotos.setWindowTitle("Інформаційне вікно системи")
        self.successedMakingPhotos.exec_()


        self.OpenCvManager.TrainPhotos(self.dataBaseManager)


    def ReadDataFromWorkerField(self):
        try:
            self.dataBaseManager.AddWorkerToDB(pid=random.randint(0, 999999),
                                               name=self.firstNameLine.text(),
                                               surname=self.secondNameLine.text(),
                                               department=self.instituteLine.text())
            return True
        except:
            print("Cannot register person in database. Please try again")
            return  False




    def ReadDataFromStudentField(self):
        try:
            self.dataBaseManager.AddStudentToDB(pid=random.randint(0, 999999),
                                                name=self.firstNameLine.text(),
                                                surname=self.secondNameLine.text(),
                                                group=self.groupLine.text())
            self.instituteLine.text()
            return True
        except:
            print("Cannot register person in database. Please try again")
            return False

    def ReadDataFromTeacherField(self):
        try:
            self.dataBaseManager.AddTeacherToDB(pid=random.randint(0, 999999),
                                                name=self.firstNameLine.text(),
                                                surname=self.secondNameLine.text(),
                                                department=self.instituteLine.text(),
                                                profession=self.professionLine.text())
            return True
        except:
            print("Cannot register person in database. Please try again")
            return False

    def ChangeUi(self):
        currentItem = self.comboBox.currentText()
        if currentItem == "Викладач":
            try:
                self.DeleteStudentUI()
            except:
                print("There isnt student ui")
            self.SetTeacherUi()
        elif currentItem == "Працівник":
            try:
                self.DeleteTeacherUI()
            except:
                print("There isnt Teacher UI")
            try:
                self.DeleteStudentUI()
            except:
                print("There isnt student ui")
        elif currentItem == "Студент":
            try:
                self.DeleteTeacherUI()
            except:
                print("There isnt Teacher UI")
            self.SetStudentUi()

    def SetTeacherUi(self):
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.professionLine = QtWidgets.QLineEdit(self.centralwidget)
        self.professionLine.setText("")
        self.professionLine.setObjectName("professionLine")
        self.professionLine.setPlaceholderText("Професор")
        self.horizontalLayout_4.addWidget(self.professionLine)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_5.setText("Посада")

    def SetStudentUi(self):
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.groupLine = QtWidgets.QLineEdit(self.centralwidget)
        self.groupLine.setText("")
        self.groupLine.setObjectName("groupLine")
        self.groupLine.setPlaceholderText("КН-412")
        self.horizontalLayout_5.addWidget(self.groupLine)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_6.setText("Група")

    def DeleteStudentUI(self):
        try:
            self.horizontalLayout_5.deleteLater()
            self.label_6.deleteLater()
            self.groupLine.deleteLater()
            self.verticalLayout.removeItem(self.horizontalLayout_5)
        finally:
            pass

    def DeleteTeacherUI(self):
        try:
            self.horizontalLayout_4.deleteLater()
            self.label_5.deleteLater()
            self.professionLine.deleteLater()
            self.verticalLayout.removeItem(self.horizontalLayout_4)
        finally:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
