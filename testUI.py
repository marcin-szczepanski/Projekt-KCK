# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(966, 587)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 121, 17))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 50, 361, 101))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 170, 71, 27))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(30, 220, 361, 241))
        self.listView.setObjectName("listView")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(450, 20, 181, 17))
        self.label_4.setObjectName("label_4")
        self.listView_2 = QtWidgets.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(450, 50, 501, 281))
        self.listView_2.setObjectName("listView_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(460, 350, 121, 17))
        self.label_6.setObjectName("label_6")
        self.listView_3 = QtWidgets.QListView(Form)
        self.listView_3.setGeometry(QtCore.QRect(550, 350, 401, 192))
        self.listView_3.setObjectName("listView_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 500, 141, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 480, 91, 17))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(20, 510, 102, 22))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 510, 102, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(100, 510, 102, 22))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(140, 510, 102, 22))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(510, 80, 56, 17))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Wprowadź wezwanie: "))
        self.label_2.setText(_translate("Form", "Rozmowa:"))
        self.pushButton.setText(_translate("Form", "Wyślij"))
        self.label_4.setText(_translate("Form", "Plan restauracji:"))
        self.label_6.setText(_translate("Form", "Uwagi i akcje:"))
        self.pushButton_3.setText(_translate("Form", "Poproś kelnera!"))
        self.label_3.setText(_translate("Form", "Wybierz stolik:"))
        self.radioButton.setText(_translate("Form", "1"))
        self.radioButton_2.setText(_translate("Form", "2"))
        self.radioButton_3.setText(_translate("Form", "3"))
        self.radioButton_4.setText(_translate("Form", "4"))
        self.label_5.setText(_translate("Form", "TextLabel"))

