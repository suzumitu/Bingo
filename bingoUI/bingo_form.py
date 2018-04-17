# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\suzum\source\repos\gitHub\Python\Bingo\bingoUI\bingo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(476, 542)
        self.btnNext = QtWidgets.QPushButton(mainForm)
        self.btnNext.setGeometry(QtCore.QRect(260, 500, 71, 23))
        self.btnNext.setObjectName("btnNext")
        self.btnExit = QtWidgets.QPushButton(mainForm)
        self.btnExit.setGeometry(QtCore.QRect(350, 500, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.label = QtWidgets.QLabel(mainForm)
        self.label.setGeometry(QtCore.QRect(40, 30, 251, 20))
        self.label.setObjectName("label")
        self.bingoTable = QtWidgets.QTableWidget(mainForm)
        self.bingoTable.setGeometry(QtCore.QRect(40, 70, 401, 401))
        self.bingoTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bingoTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bingoTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bingoTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.bingoTable.setAutoScroll(True)
        self.bingoTable.setAutoScrollMargin(16)
        self.bingoTable.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.bingoTable.setShowGrid(True)
        self.bingoTable.setRowCount(10)
        self.bingoTable.setColumnCount(10)
        self.bingoTable.setObjectName("bingoTable")
        self.bingoTable.horizontalHeader().setVisible(False)
        self.bingoTable.horizontalHeader().setDefaultSectionSize(40)
        self.bingoTable.verticalHeader().setVisible(False)
        self.bingoTable.verticalHeader().setDefaultSectionSize(40)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "ビンゴゲーム"))
        self.btnNext.setText(_translate("mainForm", "次"))
        self.btnExit.setText(_translate("mainForm", "終了"))
        self.label.setText(_translate("mainForm", "「次」ボタンをクリックすると番号が順に表示されます"))

