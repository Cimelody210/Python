import sys
from Ps import PhanSo
class DanhSachPhanSo:
    def __init__(self):
        self.dsps = []

    def themPhanSo(self, *args: PhanSo):
        for ps in args:
            self.dsps.append(ps)

    def xuat(self):
        for ps in self.dsps:
            print(ps, end="\t")

    def demPSAm(self) -> int:
        # todo: c1
        # count = 0
        # for i in self.dsps:
        #     if i.tu // i.mau < 0:
        #         count += 1
        # return count
        # todo: c2
        # return sum(
        #     1 for ps in self.dsps if ps.ktPhanSoAm())
        return len([ps for ps in self.dsps if ps.ktPhanSoAm()])

    def timTatCaVTPhanSoX(self, phan_so: PhanSo):
        result = []
        for i in range(len(self.dsps)):
            if self.dsps[i].tinhGiaTriCuaPhanSo() == \
                    phan_so.tinhGiaTriCuaPhanSo():
                result.append(i)
        return result

    def timPhanSoDuongNhoNhat(self) -> PhanSo:
        result = PhanSo(sys.maxsize, 1)
        for ps in self.dsps:
            print(ps)
            if ps > 0:
                print(ps)
                if ps < result:
                    print(ps)
                    result = ps
        return result
        # return min([ps for ps in self
        #            .dsps if ps.tinhGiaTriCuaPhanSo() > 0],
        #            key=lambda ps: ps.tinhGiaTriCuaPhanSo())

    def tinhTongCacPhanSoAm(self) -> PhanSo:
        result = PhanSo(0, 1)
        for ps in self.dsps:
            if ps.ktPhanSoAm():
                result = result.__add__(ps)
        return result

    def xoaPSX(self, phan_so: PhanSo) -> None:
        # vt = self.timTatCaVTPhanSoX(phan_so)
        # n = 0
        # for i in vt:
        #     self.dsps.pop(i - n)
        #     n += 1

        for ps in self.dsps:
            if ps.tinhGiaTriCuaPhanSo() == phan_so.tinhGiaTriCuaPhanSo():
                self.dsps.remove(ps)
                print(f'\nXoa thanh cong phan so {ps}', end="")
        print('\nXoa xong')

    def xoaTatCaPSCoTuLaX(self, tu: int) -> None:
        for ps in self.dsps:
            if ps.tu == tu:
                self.dsps.remove(ps)
                print(f'\nXoa thanh cong phan so {ps}', end="")
        print('\nXoa xong')

    def sapXepPhanSo(self, reverse: bool = False) -> None:
        self.dsps.sort(key=lambda ps: ps.tinhGiaTriCuaPhanSo(), reverse=reverse)

    def sapXepPhanSoTheoTu(self, reverse: bool = False) -> None:
        self.dsps.sort(key=lambda ps: ps.tu, reverse=reverse)

    def sapXepPhanSoTheoMau(self, reverse: bool = False) -> None:
        self.dsps.sort(key=lambda ps: ps.mau, reverse=reverse)
