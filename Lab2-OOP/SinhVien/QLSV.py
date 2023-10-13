from SInhVien import SinhVien
class QLSV:
    list =[]
    def SoLuongSV(self):
        return self.list.__len__()
    
    def NhapSV(self):
        maSo = int(input("Nhap ma so sinh vien: "))
        hoTen = str(input("Nhập họ tên: "))
        ngaySinh = str(input("Nhập ngày sinh: "))
        diemRL = int(input("Nhập điểm rèn luyện: "))
        sv = SinhVien(maSo, hoTen, ngaySinh, diemRL)
        self.list.append(sv)
    def Update(self, mssv):
        sv:SinhVien = self.TimSV_TheoMSSV(mssv)
        if sv != None:    
            maSo = int(input("Nhap ma so sinh vien: "))
            hoTen = str(input("Nhập họ tên: "))
            ngaySinh = str(input("Nhập ngày sinh: "))
            # diemRL = int(input("Nhập điểm rèn luyện: "))
            sv.maSo = maSo
            sv.hoTen = hoTen
            sv.ngaySinh = ngaySinh
            # sv.diemRL= diemRL
        else:
            print("Không tồn tại sinh viên có mã số {}".format(mssv))
   
    def DocFile(self):
        f = open("Lab2-OOP\SinhVien\dssv.txt",mode='r', encoding='UTF-8')
        with open('Lab2-OOP\SinhVien\dssv.txt',mode='r', encoding='UTF-8') as f:
            for hang in f:
                data =  hang.split(',')
                id = int(data[0])
                full_name = data[1]
                if len(full_name) >=14:
                    full_name = data[1]
                date_of_birth = data[2]
                # date_of_birth = datetime.strftime(data[2],'%-d%-m%Y')
                Score_Rl = int(data[3])
                hang =SinhVien(id, full_name, date_of_birth, Score_Rl)
                print(hang)
        f.close()
        # i =1
        # for line in f:
        #     stt =str(i)+'\t'+line
        #     i+=1
        #     if len(stt) >= 20:
        #         print(stt)
        #     else:
        #         print('*****')
    def TimSV_TheoMSSV(self, mssv:int):
        kq =None
        if self.SoLuongSV() >0:
            for sv in self.list:
                if sv.maSo ==mssv:
                    kq = sv
        return kq
    def TimVT_TheoMSSV(self, mssv:int):
        for sv in range(len(self.list)):
            if self.list[sv].mssv == mssv:
                return sv
        return -1
    def XoaSV_TheoMSSV(self, mssv:int) ->bool:
        vitri = self.TimSV_TheoMSSV(mssv)
        if vitri != -1:
            del self.list[vitri]
            return True
        else:
            return False
    def TimSV_TheoTen(self, name:str):
        ds =[]
        if self.SoLuongSV() >0:
            for sv in self.list:
                if (name.upper() in sv.hoTen.upper()):
                    list.append(sv)
        return list
    def show(self, listSV): 
        print("\t\t{:<8} {:<18} {:<8}".format("MSSV", "Họ và tên", "Ngày sinh",'Điểm rèn luyện'))
        if listSV.__len__() > 0:
            for sv in listSV:
                print("\t\t{:<8} {:<18} {:<8}".format(sv.maSo, sv.hoTen, sv.ngaySinh, sv.diemRL))
    def TangTheoTen(self):
        self.list.sort(key = lambda x: x.hoTen, reverse=False)
    def GetListSV(self):
        return self.list
