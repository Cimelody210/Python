from datetime import datetime
class SinhVien:
    def __init__(self,maSo:int,hoTen:str,ngaySinh:datetime) -> None:
        self._maSo=maSo
        self._hoTen=hoTen
        self._ngaySinh=ngaySinh
        
    @property
    def MaSo(self):
        return self._maSo
    
    @property
    def HoTen(self):
        return self._hoTen
    
    @property
    def NgaySinh(self):
        return self._ngaySinh
    
    @HoTen.setter
    def hoTen(self,hoTen:str):
        self._hoTen=hoTen
        
    @MaSo.setter
    def MaSo(self,maSo:int):
        if self.KiemTraMaSoHopLe(maSo):
            self._maSo=maSo
    
    @staticmethod
    def KiemTraMaSoHopLe(ms:int):
        return len(str(ms))== 7
        
    def __str__(self) -> str:
        return f"{self.MaSo}\t\t{self.HoTen}\t\t{self.NgaySinh}"