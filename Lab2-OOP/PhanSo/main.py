from DS_PhanSo import DanhSachPhanSo
from Ps import PhanSo
def main():
    print('''''')
    phanSo1 = PhanSo(-2, 3)
    phanSo2 = PhanSo(3, 5)
    phanSo3 = PhanSo(100, 5)
    phanSo4 = PhanSo(100, 25)
    phanSo5 = PhanSo(2, 3)
    phanSo6 = PhanSo(-8, 3)
    phanSo7 = PhanSo(2, 3)
    phanSo8 = PhanSo(-9, 3)
    phanSo9 = PhanSo(-100, 3)
    phanSo10 = PhanSo(100, 4)
    phanSo11 = PhanSo()
    while True:
        n = int(input("Nhập lựa chọn ở đây: "))
        if n ==1:
            print(f'{phanSo1} + {phanSo2} = {phanSo1.__add__(phanSo2)} ')
            print(f'{phanSo1} - {phanSo2} = {phanSo1.__sub__(phanSo2)} ')
            print(f'{phanSo1} * {phanSo2} = {phanSo1.__mul__(phanSo2)} ')
            print(f'{phanSo1} : {phanSo2} = {phanSo1.__truediv__(phanSo2)} ')
            phanSo1.rutGon()
            print(phanSo10)
        elif n==2:
            dsPhanSo = DanhSachPhanSo()
            dsPhanSo.themPhanSo(phanSo1, phanSo2, phanSo3, phanSo4, phanSo5, phanSo6, phanSo7, phanSo8, phanSo9, phanSo10, phanSo11)
            print("Danh sach phan so la: ")
            dsPhanSo.xuat()
        elif n==3:
            dsPhanSo = DanhSachPhanSo()
            print(f"\nSo phan so am la: {dsPhanSo.demPSAm()}")
        elif n==4:
            dsPhanSo = DanhSachPhanSo()
            print(f"Phan so duong nho nhat la: {dsPhanSo.timPhanSoDuongNhoNhat()}")
            # phanSoTim = PhanSo(2, 3)
            # print(f"Cac vi tri phan so {phanSoTim} la: ")
            # kq = dsPhanSo.TimTatCaVTPhanSoX(phanSoTim)
            # for i in kq:
            #     print(i + 1, end="\t")
        elif n==5:
            dsPhanSo = DanhSachPhanSo()
            print(f'\nTong cac phan so am la: {dsPhanSo.tinhTongCacPhanSoAm()}')
            # dsPhanSo.xoaPSX(PhanSo(2, 3))
            # dsPhanSo.xoaTatCaPSCoTuLaX(20)
            # print(f'\nMang sau khi xoa: ')
            # print('\nSau khi sap xep: ')
            # todo: if true giam
            #  mac dinh tang
            # dsPhanSo.sapXepPhanSo()
            # dsPhanSo.sapXepPhanSo(True)
            # dsPhanSo.sapXepPhanSoTheoTu()
            # dsPhanSo.sapXepPhanSoTheoTu(True)
            # dsPhanSo.sapXepPhanSoTheoMau()
            # dsPhanSo.sapXepPhanSoTheoMau(True)
            dsPhanSo.xuat()

main()
