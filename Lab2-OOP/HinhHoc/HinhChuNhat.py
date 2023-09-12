from HinhHoc import HinhHoc
class HinhChuNhat(HinhHoc):
    def __init__(self, canh: float,chieurong:float,chieudai:float) -> None:
        super().__init__(canh)
        self.chieudai=chieudai
        self.chieurong=chieurong
    
    def TinhDT(self):
        return (self.chieuDai * self.chieuRong)
    def __str__(self) -> str:
        return super().__str__()+f"Hình chữ nhật có chiều dài = {self.chieudai} và chiều rộng {self.chieurong} "
    

        