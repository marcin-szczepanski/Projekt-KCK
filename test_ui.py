# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(966, 587)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 50, 361, 101))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 170, 71, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(30, 220, 361, 261))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 260, 241, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(450, 20, 181, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.listView_2 = QtGui.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(450, 50, 501, 281))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(480, 70, 251, 81))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(460, 350, 121, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.listView_3 = QtGui.QListView(Form)
        self.listView_3.setGeometry(QtCore.QRect(550, 350, 401, 192))
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 500, 141, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 500, 141, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Wprowadź wezwanie: ", None))
        self.label_2.setText(_translate("Form", "Odpowiedź kelnera:", None))
        self.pushButton.setText(_translate("Form", "Wyślij", None))
        self.label_3.setText(_translate("Form", "Tu będą się pojawiać odpowiedzi kelnera :)", None))
        self.label_4.setText(_translate("Form", "Plan restauracji:", None))
        self.label_5.setText(_translate("Form", "Tu będzie plan z rozmieszczeniem stolików.", None))
        self.label_6.setText(_translate("Form", "Uwagi i akcje:", None))
        self.pushButton_2.setText(_translate("Form", "Wejdź do restauracji!", None))
        self.pushButton_3.setText(_translate("Form", "Poproś kelnera!", None))

