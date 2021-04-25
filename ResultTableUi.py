# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResultTable.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableResultWindow(object):
    def setupUi(self, MainWindow, listOfPersons):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
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

        self.tableWidget.setRowCount(len(listOfPersons))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(("Ім\'я", "Прізвище", "Дата", "Час входу", "Час виходу"))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        print(listOfPersons)
        correctViewResultTable = list()
        for obj in listOfPersons:
            name = obj[1]
            surname = obj[2]
            date = obj[3].date()
            enterTime = obj[3].time()
            try:
                exitTime = obj[4].time()
            except:
                exitTime = '-'
            correctViewResultTable.append((name, surname, date, enterTime, exitTime))

        for obj in correctViewResultTable:
            for j in range(len(obj)):
                self.tableWidget.setItem(correctViewResultTable.index(obj), j, QtWidgets.QTableWidgetItem(str(obj[j])))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RegisterWorkerWindow"))
        self.label.setText(_translate("MainWindow", "---Вікно зареєстрованих осіб---"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
