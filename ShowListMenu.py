# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newregisterwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowListWindow(object):
    def setupUi(self, MainWindow, DataBaseManager):
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
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout.addWidget(self.dateTimeEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.auditory = QtWidgets.QLabel(self.centralwidget)
        self.auditory.setObjectName("auditory")
        self.horizontalLayout_3.addWidget(self.auditory)
        self.auditoryLine = QtWidgets.QLineEdit(self.centralwidget)
        self.auditoryLine.setText("")
        self.auditoryLine.setObjectName("auditoryLine")
        self.horizontalLayout_3.addWidget(self.auditoryLine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.showListButton = QtWidgets.QPushButton(self.centralwidget)
        self.showListButton.setObjectName("showListButton")
        self.verticalLayout_2.addWidget(self.showListButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
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

        # connect to buttons
        self.showListButton.clicked.connect(self.PrintPersons)
        self.retranslateUi(MainWindow)

        self.DBManager = DataBaseManager

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RegisterStudentWindow"))
        self.label.setText(_translate("MainWindow", "Виберіть бажану дату та час"))
        self.auditory.setText(_translate("MainWindow", "Аудиторія"))
        #self.auditoryLine.setPlaceholderText(_translate("MainWindow", "e.g. IKNI"))
        self.showListButton.setText(_translate("MainWindow", "Показати список присутніх людей"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    def PrintPersons(self):
        # delete
        try:
            self.tableWidget.deleteLater()
            self.verticalLayout.removeItem(self.tableWidget)
        except:
            print("No table to delete")
         
        listOfPids = self.DBManager.GetCurrentVisitorsList(self.dateTimeEdit.date(), self.dateTimeEdit.time())
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(len(listOfPids))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(("Ім\'я", "Прізвище"))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        print(listOfPids)
        for obj in listOfPids:
            print(obj)
            for j in range(len(obj)):
                print(listOfPids.index(obj), j, obj[j])
                self.tableWidget.setItem(listOfPids.index(obj), j, QtWidgets.QTableWidgetItem(obj[j]))
        self.verticalLayout.addWidget(self.tableWidget)


