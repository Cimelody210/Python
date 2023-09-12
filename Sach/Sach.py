class Sach:
    def __init__(self, tensach:str, tentacgia:str, ngayxuatban:str, sotrang:int, giabia:int) -> None:
        self.tensach=tensach
        self.tentacgia= tentacgia
        self.ngayxuatban = ngayxuatban
        self.sotrang = sotrang
        self.giabia =giabia
    def __str__(self) -> str:
        return f'{self.tensach} \t {self.tentacgia} \t {self.ngayxuatban} \t {self.sotrang} \t {self.giabia}'
