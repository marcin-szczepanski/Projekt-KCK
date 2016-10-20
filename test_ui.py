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
        self.listView.setGeometry(QtCore.QRect(30, 220, 361, 241))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(450, 20, 181, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.listView_2 = QtGui.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(450, 50, 501, 281))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(460, 350, 121, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.listView_3 = QtGui.QListView(Form)
        self.listView_3.setGeometry(QtCore.QRect(550, 350, 401, 192))
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 500, 141, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 480, 91, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(20, 510, 102, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 510, 102, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(100, 510, 102, 22))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(140, 510, 102, 22))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Wprowadź wezwanie: ", None))
        self.label_2.setText(_translate("Form", "Rozmowa:", None))
        self.pushButton.setText(_translate("Form", "Wyślij", None))
        self.label_4.setText(_translate("Form", "Plan restauracji:", None))
        self.label_6.setText(_translate("Form", "Uwagi i akcje:", None))
        self.pushButton_3.setText(_translate("Form", "Poproś kelnera!", None))
        self.label_3.setText(_translate("Form", "Wybierz stolik:", None))
        self.radioButton.setText(_translate("Form", "1", None))
        self.radioButton_2.setText(_translate("Form", "2", None))
        self.radioButton_3.setText(_translate("Form", "3", None))
        self.radioButton_4.setText(_translate("Form", "4", None))

