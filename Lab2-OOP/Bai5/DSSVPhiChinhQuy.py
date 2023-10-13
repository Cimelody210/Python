from datetime import datetime
from SInhVien import SinhVien
class DSSVPhiChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime,trinhDo:str,tgdt:int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.trinhdo=trinhDo
        self.tgdt=tgdt
        
    def __str__(self) -> str:
        return super().__str__()+ f"\t{self.trinhdo} \t {self.tgdt}"
    