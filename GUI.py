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
        MainWindow.setWindowIcon((QIcon('icon.png')) )
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
        self.Wpisywanie = QtWidgets.QLineEdit(self.centralwidget)
        self.Wpisywanie.setGeometry(QtCore.QRect(130, 600, 221, 31))
        self.Wpisywanie.setObjectName("Wpisywanie")
        self.Wpisywanie.returnPressed.connect(self.Wyslanie)
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
        self.label_menu.hide()
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
        self.Menu.hide()
        self.Stolik = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Stolik.setGeometry(QtCore.QRect(800, 300, 291, 331))
        self.Stolik.setObjectName("Stolik")
        self.Stolik.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        text = codecs.open("menuPLN.txt", "r", "utf-8").read()
        a=text.replace(";","    ")
        self.Menu.insertPlainText(a)
        self.podane=0
        self.podanemenu=0
        self.kelner_przy_stoliku=0
        self.numerstolika=0
        MainWindow.setStatusBar(self.statusbar)
        msg = QtWidgets.QInputDialog()
        msg.isComboBoxEditable()
        msg.setLabelText("Wybierz stolik")
        a=("1","2","3","4")
        msg.setComboBoxItems(a)
        msg.setWindowTitle("Wybór stolika")
        msg.setWindowIcon(QIcon('icon.png'))
        retval = msg.exec_()
        if retval == 0:
            sys.exit()
        self.numerstolika=msg.textValue()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automatyczny kelner - Projekt KCK"))
        self.Wyslij.setText(_translate("MainWindow", "Wyślij"))
        self.label_rozmowa.setText(_translate("MainWindow", "Rozmowa"))
        self.label_komunikaty.setText(_translate("MainWindow", "Komunikaty"))
        self.label_menu.setText(_translate("MainWindow", "Menu"))
        self.label_stolik.setText(_translate("MainWindow", "Stolik"))
        self.Kelner.setText(_translate("MainWindow", "Zawołaj kelnera"))

    def Wyslanie(self):  #pobieranie tekstu wpisywanego przez klienta i wypisywanie go w logach
        wpisywany_in= self.Wpisywanie.text()
        if self.kelner_przy_stoliku!=0:
            if len(wpisywany_in)>0:
                wpisywany_out="Klient: "+wpisywany_in+"\n"
                self.Logi.insertPlainText(wpisywany_out)
                odpowiedz_in="to odp kelnera"
                self.OdpowiedzKelnera(odpowiedz_in)
                blablabla="konmunikat1"
                self.Komunikowanie(blablabla)
                self.Wpisywanie.clear()
                #logit = open("log.txt", "a")
                #logit.write(self.Logi.toPlainText())
                #logit.close()
                if wpisywany_in=="dawaj jedzenie":  ##podanie jedzenia
                    self.PodajJedzenie()
                if wpisywany_in=="podaj menu":
                    self.PodajMenu()
                if wpisywany_in=="zabierz menu":
                    self.ZabierzMenu()
                if wpisywany_in=="podaj danie":
                    jedzonko="bułka z chlebem"
                    self.PodajDanie(jedzonko)
                if wpisywany_in=="zabierz jedzenie":
                    self.ZabierzJedzenie()
            else:
                self.Komunikowanie("Wpisz tekst przed wysłaniem!")
        else:
            self.Komunikowanie("Aby porozmawiać z kelnerem musisz najpierw go zawołać.")


    def PodajMenu(self):
                    self.Menu.show()
                    self.label_menu.show()

    def ZabierzMenu(self):
                    self.Menu.hide()
                    self.label_menu.hide()

    def PodajDanie(self, podane_danie_in):
        """
        :type podane_danie_in: string
        """
        podane_danie_out=podane_danie_in+"\n"
        self.Stolik.insertPlainText(podane_danie_out)
        self.PodajJedzenie()

    def PodajJedzenie(self):
         self.podane=1
         if "1" == self.numerstolika:
            self.label_obraz.setPixmap(QtGui.QPixmap("j1.jpg"))
         if "2" == self.numerstolika:
            self.label_obraz.setPixmap(QtGui.QPixmap("j2.jpg"))
         if "3" == self.numerstolika:
            self.label_obraz.setPixmap(QtGui.QPixmap("j3.jpg"))
         if "4" == self.numerstolika:
            self.label_obraz.setPixmap(QtGui.QPixmap("j4.jpg"))

    def WolajKelnera(self): #zawołanie kelnera
        self.kelner_przy_stoliku=1
        if self.podane==0:
            if "1" == self.numerstolika:
                self.label_obraz.setPixmap(QtGui.QPixmap("w1.jpg"))
            if "2" == self.numerstolika:
                self.label_obraz.setPixmap(QtGui.QPixmap("w2.jpg"))
            if "3" == self.numerstolika:
                self.label_obraz.setPixmap(QtGui.QPixmap("w3.jpg"))
            if "4" == self.numerstolika:
                self.label_obraz.setPixmap(QtGui.QPixmap("w4.jpg"))
        else:
            if "1" == self.numerstolika:
                self.label_obraz.setPixmap(QtGui.QPixmap("p1.jpg"))
            if "2" == self.numerstolika:
                self.label_obraz.setPixmap(QtGui.QPixmap("p2.jpg"))
            if "3" == self.numerstolika:
                self.label_obraz.setPixmap(QtGui.QPixmap("p3.jpg"))
            if "4" == self.numerstolika:
                self.label_obraz.setPixmap(QtGui.QPixmap("p4.jpg"))

    def ZabierzJedzenie(self):
         self.podane=0
         if "1" == self.numerstolika:
            self.label_obraz.setPixmap(QtGui.QPixmap("w1.jpg"))
         if "2" == self.numerstolika:
            self.label_obraz.setPixmap(QtGui.QPixmap("w2.jpg"))
         if "3" == self.numerstolika:
            self.label_obraz.setPixmap(QtGui.QPixmap("w3.jpg"))
         if "4" == self.numerstolika:
            self.label_obraz.setPixmap(QtGui.QPixmap("w4.jpg"))

    def Komunikowanie(self, komunikat_in):
         """
         :type komunikat_in: string
         """
         komunikat_out=komunikat_in+"\n"
         self.Komunikaty.insertPlainText(komunikat_out)

    def OdpowiedzKelnera(self, odp_kelnera_in):
         """
         :type odp_kelnera_in: string
         """
         odp_kelnera_out="Kelner:"+odp_kelnera_in+"\n"
         self.Logi.insertPlainText(odp_kelnera_out)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            print("esc")






if __name__ == "__main__":  #wyswietlanie grafiki - start
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
