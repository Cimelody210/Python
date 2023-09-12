# from datetime import datetime
from Sach import Sach    
from DSSach import DSSach

def Main():
    ds_sach = DSSach()
    ds_sach.ds.append(Sach('Sach 1','Shakepears','2000-01-01',150,50))
    ds_sach.ds.append(Sach('Sach 2','Author C','1864-04-11',120,60))
    ds_sach.ds.append(Sach('Sach 3','Toriyama Akira','1927-01-01',90,50))
    ds_sach.ds.append(Sach('Sach 4','Shakepears','1837-11-26',200,50))
    ds_sach.ds.append(Sach('Sach 5','Juan de Nova','1956-12-21',80,50))
    ds_sach.ds.append(Sach('Sach 6','Arthur ConanDoyle','1836-01-01',180,50))

    ds_sach.__str__()
    sach_nam_2000 = ds_sach.TimTheoNam(2000)
    for sach in sach_nam_2000.ds:
        print(sach.tensach)
    sach_shakepear = ds_sach.TimTheoTacGia('Shakepears')
    for sach in sach_shakepear.ds:
        print(sach.tensach)

    sach_tren100Trang = ds_sach.TimTheoSoTrang(100)
    for sach in sach_tren100Trang.ds:
        print(sach.tensach)


    # ds_sach.SapXepTheoTG()
    # ds_sach.SapXepTheoNamxb()
    for sach in ds_sach.ds:
        print(sach.tensach)

Main()