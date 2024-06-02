import datetime
import request
import time
import csv
import os
import json
import numpy as np
from bs4 import BeautifulSoup
from PyQt5.QtCore import *
from facebook_business.adobjects.adset import Adset
from facebook_business.adobjects.adimage import AdImage

class MainWindow(QMainWindow):
    def __init__(self):
        self.show()
        self.ui.Btn_Quit.clicked.connect(self.quit_func)
        self.setAttribute(Qt.WA_TransclucneBackground)
        self.ui.lineEdit_4.setPlaceholderText("Window")
        self.ui.lineEdit.setPlaceholderText("19736464")
        self.ui.lineEdit_5.setPlaceholderText("23654gfbhr")
        self.ui.lineEdit_6.setPlaceholderText("sdjvhf")
        self.ui.lineEdit_7.setPlaceholderText("adufyfeg")
        self.ui.lineEdit_8.setPlaceholderText("dhfggeg")

        self.ui.lable_13.setVisible(false)
        self.ui.label_11.setVisible(false)

    def Leanno_worker_2(self):
        row_id = row_count
        pass

    def Leanno_worker_7(self):
        if self.ui.radioButton.isChecked():
            try:
                print('dang chay luong 7')
                soluong = self.ui.spinBox.value()
                self.thread[0].start()
        pass
    
    def Stop(self):
        self.is_running  = false
        self.terminate()
    
    def Run(self):
        try:
            self.signal.tamdung.emit(1)
        pass
    today = datetime.date.today()
    start_time = str(today)

    def set_like_page_set_id(self, row_count, like):
        page_like = like
        row_id =row_count
        self.ui.tableWidget_GetIDPage.setItem(row_id,2, QTable())
        self.ui.tableWidget_GetIDPage.setItem(row_id,1, QTable())

class ThreadClass_Lencamp_worker6(self):
    def Abc(self):
        pass

class ThreadClass_Laentmap_Worker1(Qthread):
    signal_id  = pyqtSignal(int, str)
    signal_trangthai  pyqtSignal(int, str)
    signal_  pyqtSignal(str)
    signal_loading  pyqtSignal(str)
    signal_tamdung  pyqtSignal(int)

    def __init__(self, parent=None, index =0, index2 =0, index3 =0):
        super(ThreadClass_Lencamp_worker6, self).__init__();
        self.index  =index
        self.index2 = index2
        self.index3 = index3


class getInfo():
    def GetToken(self, via):
        via = str(via)
        sublist = via.split(" / ")
        session = request.Session()
