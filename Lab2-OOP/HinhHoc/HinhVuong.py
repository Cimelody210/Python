from HinhHoc import HinhHoc
class HinhVuong(HinhHoc):
    def __init__(self, canh: float) -> None:
        super().__init__(canh)
        self.canh=canh
        
    def __str__(self) -> str:
        return super().__str__()+f" Hình vuông có cạnh là = {self.canh} "
    
    
        