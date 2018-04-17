# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:03:36 2017

@author: suzumitu
"""

import sys
import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QTableWidgetItem, QApplication)
from bingoUI import bingo_form
import random

SCRIPTDIR =  os.path.abspath(os.path.dirname(__file__))

class BingoForm(QWidget):
    kth = 0
    bingoList = list(range(1,100))
    random.shuffle(bingoList)

    def __init__(self):
        super().__init__()
        self.ui = bingo_form.Ui_mainForm()
        self.ui.setupUi(self)
        self.initUI()
        random.seed()

    def initUI(self):
        #for i in range(10):
        #    for j in range(10):
        #        item = QTableWidgetItem(str(10*i + j + 1).rjust(5))
        #        self.ui.bingoTable.setItem(i, j, item)
        self.setWindowIcon(QtGui.QIcon(os.path.join(SCRIPTDIR, 'bingo.ico')))
        self.ui.btnExit.clicked.connect(self.btnExitClicked)
        self.ui.btnNext.clicked.connect(self.next)

    def btnExitClicked(self):
        self.close()

    def getIndex(self, nums):
        indices = []
        for num in nums:
            num = num - 1
            i = num // 10
            j = num % 10
            indices.append((i, j))
        return indices

    def deselect(self):
        if self.kth > 0:
            bingoNum = self.bingoList[self.kth - 1] - 1
            i = bingoNum // 10
            j = bingoNum % 10
            self.ui.bingoTable.item(i, j).setSelected(False)

    def next(self):
        bingoNum = self.bingoList[self.kth] - 1
        i = bingoNum // 10
        j = bingoNum % 10
        item = QTableWidgetItem(str(10*i + j + 1).rjust(5))
        self.ui.bingoTable.setItem(i, j, item)
        self.ui.bingoTable.item(i, j).setSelected(True)
        self.deselect()

        self.kth += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = BingoForm()
    form.show()
    sys.exit(app.exec_())
