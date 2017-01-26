# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1215, 691)
        MainWindow.setWindowTitle("Automatyczny kelner - KCK")
        MainWindow.setWindowIcon(QIcon('icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logi = QtWidgets.QTextEdit(self.centralwidget)
        self.Logi.setGeometry(QtCore.QRect(130, 300, 291, 301))
        self.Logi.setReadOnly(True)
        self.Logi.setObjectName("Logi")
        self.Logi.isReadOnly()
        self.Wyslij = QtWidgets.QPushButton(self.centralwidget)
        self.Wyslij.setGeometry(QtCore.QRect(350, 600, 71, 31))
        self.Wyslij.setObjectName("Wyslij")
        self.Wyslij.clicked.connect(self.Wyslanie)
        self.Komunikaty = QtWidgets.QTextEdit(self.centralwidget)
        self.Komunikaty.setGeometry(QtCore.QRect(130, 30, 291, 221))
        self.Komunikaty.setReadOnly(True)
        self.Komunikaty.setObjectName("Komunikaty")
        self.Wpisywanie = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Wpisywanie.setGeometry(QtCore.QRect(130, 600, 221, 31))
        self.Wpisywanie.setObjectName("Wpisywanie")
        self.Stolik = QtWidgets.QTableWidget(self.centralwidget)
        self.Stolik.setGeometry(QtCore.QRect(800, 300, 291, 331))
        self.Stolik.setObjectName("Stolik")
        self.Stolik.setColumnCount(2)
        self.Stolik.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.Stolik.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stolik.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stolik.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stolik.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stolik.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stolik.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stolik.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Stolik.setItem(1, 1, item)
        self.Menu = QtWidgets.QTableWidget(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(460, 300, 291, 331))
        self.Menu.setObjectName("Menu")
        self.Menu.setColumnCount(2)
        self.Menu.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.Menu.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Menu.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Menu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Menu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Menu.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Menu.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Menu.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Menu.setItem(1, 1, item)
        self.label_obraz = QtWidgets.QLabel(self.centralwidget)
        self.label_obraz.setGeometry(QtCore.QRect(650, 0, 441, 261))
        self.label_obraz.setText("")
        self.label_obraz.setPixmap(QtGui.QPixmap("restauracja1.jpg"))
        self.label_obraz.setScaledContents(True)
        self.label_obraz.setObjectName("label_obraz")
        self.Stolik1 = QtWidgets.QCheckBox(self.centralwidget)
        self.Stolik1.setGeometry(QtCore.QRect(580, 70, 70, 17))
        self.Stolik1.setChecked(False)
        self.Stolik1.setObjectName("Stolik1")
        self.Stolik2 = QtWidgets.QCheckBox(self.centralwidget)
        self.Stolik2.setGeometry(QtCore.QRect(580, 100, 70, 17))
        self.Stolik2.setObjectName("Stolik2")
        self.Stolik3 = QtWidgets.QCheckBox(self.centralwidget)
        self.Stolik3.setGeometry(QtCore.QRect(580, 130, 70, 17))
        self.Stolik3.setChecked(True)
        self.Stolik3.setObjectName("Stolik3")
        self.Stolik4 = QtWidgets.QCheckBox(self.centralwidget)
        self.Stolik4.setGeometry(QtCore.QRect(580, 160, 70, 17))
        self.Stolik4.setObjectName("Stolik4")
        self.label_rozmowa = QtWidgets.QLabel(self.centralwidget)
        self.label_rozmowa.setGeometry(QtCore.QRect(220, 270, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_rozmowa.setFont(font)
        self.label_rozmowa.setObjectName("label_rozmowa")
        self.label_komunikaty = QtWidgets.QLabel(self.centralwidget)
        self.label_komunikaty.setGeometry(QtCore.QRect(220, 0, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_komunikaty.setFont(font)
        self.label_komunikaty.setObjectName("label_komunikaty")
        self.label_menu = QtWidgets.QLabel(self.centralwidget)
        self.label_menu.setGeometry(QtCore.QRect(580, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_menu.setFont(font)
        self.label_menu.setObjectName("label_menu")
        self.label_stolik = QtWidgets.QLabel(self.centralwidget)
        self.label_stolik.setGeometry(QtCore.QRect(920, 270, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_stolik.setFont(font)
        self.label_stolik.setObjectName("label_stolik")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.Wyslij.setText(_translate("MainWindow", "Wyślij"))
        item = self.Stolik.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nowy wiersz"))
        item = self.Stolik.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nowy wiersz"))
        item = self.Stolik.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nowa kolumna"))
        item = self.Stolik.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nowa kolumna"))
        __sortingEnabled = self.Stolik.isSortingEnabled()
        self.Stolik.setSortingEnabled(False)
        item = self.Stolik.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Stolik.item(0, 1)
        item.setText(_translate("MainWindow", "2"))
        item = self.Stolik.item(1, 0)
        item.setText(_translate("MainWindow", "3"))
        item = self.Stolik.item(1, 1)
        item.setText(_translate("MainWindow", "4"))
        self.Stolik.setSortingEnabled(__sortingEnabled)
        item = self.Menu.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nowy wiersz"))
        item = self.Menu.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nowy wiersz"))
        item = self.Menu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nowa kolumna"))
        item = self.Menu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nowa kolumna"))
        __sortingEnabled = self.Menu.isSortingEnabled()
        self.Menu.setSortingEnabled(False)
        item = self.Menu.item(0, 0)
        item.setText(_translate("MainWindow", "a"))
        item = self.Menu.item(0, 1)
        item.setText(_translate("MainWindow", "b"))
        item = self.Menu.item(1, 0)
        item.setText(_translate("MainWindow", "c"))
        item = self.Menu.item(1, 1)
        item.setText(_translate("MainWindow", "d"))
        self.Menu.setSortingEnabled(__sortingEnabled)
        self.Stolik1.setText(_translate("MainWindow", "Stolik 1"))
        self.Stolik2.setText(_translate("MainWindow", "Stolik 2"))
        self.Stolik3.setText(_translate("MainWindow", "Stolik 3"))
        self.Stolik4.setText(_translate("MainWindow", "Stolik 4"))
        self.label_rozmowa.setText(_translate("MainWindow", "Rozmowa"))
        self.label_komunikaty.setText(_translate("MainWindow", "Komunikaty"))
        self.label_menu.setText(_translate("MainWindow", "Menu"))
        self.label_stolik.setText(_translate("MainWindow", "Stolik"))

    def Wyslanie(self):  #pobieranie tekstu wpisywanego przez klienta i wypisywanie go w logach
        wpisywany_in= self.Wpisywanie.toPlainText()
        wpisywany_out="Klient: "+wpisywany_in+"\n"
        self.Logi.insertPlainText(wpisywany_out)
        odpowiedz_in="to odp kelnera"
        odpowiedz_out="Kelner: "+odpowiedz_in+"\n"
        self.Logi.insertPlainText(odpowiedz_out)
        self.Komunikowanie()
        self.Wpisywanie.clear()
        #item = self.Menu.horizontalHeaderItem(2)
        #item.setText("Nowa kolumna")
        #item = self.Menu.item(1, 1)
        #item.setText("z")
        #self.Menu.setRowCount(2)

    def Komunikowanie(self):
        komunikat_in="komunikat 1"
        komunikat_out=komunikat_in+"\n"
        self.Komunikaty.insertPlainText(komunikat_out)



if __name__ == "__main__":  #wyswietlanie grafiki - start
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #ui.label_obraz.setPixmap(QtGui.QPixmap("restauracja2.jpg"))
    #s="xcv"
    #ui.Logi.setPlainText(s)    #ustawienie tekstu ze stringa
    #g=ui.Logi.toPlainText()  #pobranie stringa z pola
    #ui.Wpisywanie.insertPlainText(g)
    #ui.Logi.insertPlainText(ui.Wpisywanie.toPlainText())#wstawienie
    sys.exit(app.exec_())
