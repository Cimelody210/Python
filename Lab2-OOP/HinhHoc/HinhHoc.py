import os
from HinhChuNhat import HinhChuNhat
from HinhVuong import HinhVuong
from HinhTron import HinhTron
class HinhHoc:
    def __init__(self,canh:float) -> None:
        self.__canh=canh
    
    @property
    def Canh(self):
        return self.__canh
    
    @Canh.setter
    def Canh(self,canh):
        self.Canh=canh
    