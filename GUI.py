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
from PyQt5.QtCore import pyqtSlot
import sys
import codecs




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1215, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logi = QtWidgets.QTextEdit(self.centralwidget)
        self.Logi.setGeometry(QtCore.QRect(130, 300, 291, 301))
        self.Logi.setReadOnly(True)
        self.Logi.setObjectName("Logi")
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
        #self.Wpisywanie.keyPressEvent.connect(self.Wyslanie)
        self.label_obraz = QtWidgets.QLabel(self.centralwidget)
        self.label_obraz.setGeometry(QtCore.QRect(650, 0, 441, 261))
        self.label_obraz.setText("")
        self.label_obraz.setPixmap(QtGui.QPixmap("restauracja1.jpg"))
        self.label_obraz.setScaledContents(True)
        self.label_obraz.setObjectName("label_obraz")
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
        self.Kelner = QtWidgets.QPushButton(self.centralwidget)
        self.Kelner.setGeometry(QtCore.QRect(350, 640, 91, 31))
        self.Kelner.setObjectName("Kelner")
        self.Kelner.clicked.connect(self.WolajKelnera)
        self.Menu = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(470, 300, 291, 331))
        self.Menu.setObjectName("Menu")
        self.Menu.setReadOnly(True)
        self.Stolik = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Stolik.setGeometry(QtCore.QRect(800, 300, 291, 331))
        self.Stolik.setObjectName("Stolik")
        self.Stolik.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        text = codecs.open("menu.txt", "r", "utf-8").read()
        a=text.replace(";","    ")
        self.Menu.insertPlainText(a)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(580, 150, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.nrstolika = QtWidgets.QLabel(self.centralwidget)
        self.nrstolika.setGeometry(QtCore.QRect(510, 150, 121, 21))
        self.nrstolika.setObjectName("label")
        self.podane=0
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Wyslij.setText(_translate("MainWindow", "Wyślij"))
        self.label_rozmowa.setText(_translate("MainWindow", "Rozmowa"))
        self.label_komunikaty.setText(_translate("MainWindow", "Komunikaty"))
        self.label_menu.setText(_translate("MainWindow", "Menu"))
        self.label_stolik.setText(_translate("MainWindow", "Stolik"))
        self.Kelner.setText(_translate("MainWindow", "Zawołaj kelnera"))
        self.nrstolika.setText(_translate("MainWindow", "Numer stolika:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))

    def Wyslanie(self):  #pobieranie tekstu wpisywanego przez klienta i wypisywanie go w logach
        wpisywany_in= self.Wpisywanie.toPlainText()
        self.comboBox.setEnabled(0)
        if len(wpisywany_in)>0:
            wpisywany_out="Klient: "+wpisywany_in+"\n"
            self.Logi.insertPlainText(wpisywany_out)
            odpowiedz_in="to odp kelnera"
            odpowiedz_out="Kelner: "+odpowiedz_in+"\n"
            self.Logi.insertPlainText(odpowiedz_out)
            self.Komunikowanie()
            self.Wpisywanie.clear()
            logit = open("log.txt", "a")
            logit.write(self.Logi.toPlainText())
            logit.close()
            if wpisywany_in=="dawaj jedzenie":  ##podanie jedzenia
                self.podane=1
                if "1" == self.comboBox.currentText():
                    self.label_obraz.setPixmap(QtGui.QPixmap("j1.jpg"))
                if "2" == self.comboBox.currentText():
                    self.label_obraz.setPixmap(QtGui.QPixmap("j2.jpg"))
                if "3" == self.comboBox.currentText():
                    self.label_obraz.setPixmap(QtGui.QPixmap("j3.jpg"))
                if "4" == self.comboBox.currentText():
                    self.label_obraz.setPixmap(QtGui.QPixmap("j4.jpg"))
        else:
            self.Komunikaty.insertPlainText("Wpisz tekst przed wysłaniem!\n")

    def WolajKelnera(self): #zawołanie kelnera
        if self.podane==0:
            if "1" == self.comboBox.currentText():
                self.label_obraz.setPixmap(QtGui.QPixmap("w1.jpg"))
            if "2" == self.comboBox.currentText():
                self.label_obraz.setPixmap(QtGui.QPixmap("w2.jpg"))
            if "3" == self.comboBox.currentText():
                self.label_obraz.setPixmap(QtGui.QPixmap("w3.jpg"))
            if "4" == self.comboBox.currentText():
                self.label_obraz.setPixmap(QtGui.QPixmap("w4.jpg"))
        else:
            if "1" == self.comboBox.currentText():
                self.label_obraz.setPixmap(QtGui.QPixmap("p1.jpg"))
            if "2" == self.comboBox.currentText():
                self.label_obraz.setPixmap(QtGui.QPixmap("p2.jpg"))
            if "3" == self.comboBox.currentText():
                self.label_obraz.setPixmap(QtGui.QPixmap("p3.jpg"))
            if "4" == self.comboBox.currentText():
                self.label_obraz.setPixmap(QtGui.QPixmap("p4.jpg"))

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
