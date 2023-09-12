from HinhHoc import HinhHoc
from math import pi
class HinhTron(HinhHoc):
    def __init__(self, canh: float, banKinh:float) -> None:
        super().__init__(canh)
        self.banKinh =banKinh
    def DTHinhTron(self):
        return pi* self.banKinh**self.banKinh
    def __str__(self) -> str:
        return super().__str__()+f'Hình tròn có bán kính = {self.banKinh}'