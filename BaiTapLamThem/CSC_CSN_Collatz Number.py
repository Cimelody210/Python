# Kiểm tra cấp số cộng, cấp số nhân
# Giả thuyết Collatz đề cập đến một dãy số xác định như sau: bắt đầu bằng một số tự nhiên n bất kỳ. Mỗi số tiếp theo được xác định theo số trước đó bằng định nghĩa sau: nếu số trước đó là một số chẵn, thì số tiếp theo bằng một nửa số trước. Nếu số trước là một số lẻ, thì số tiếp theo bằng ba lần số trước cộng với 1. Phỏng đoán cho rằng với bất kỳ giá trị nào của n, dãy số luôn luôn đạt tới 1.

import sys, os
import panda as pd

def read_all_excel(self):
    try:
        print("hdhdh")
        if os.path.isdir(self.EXCEL_FOLDER.PATH):
            excel_file = [ f for f in os.listdir(self.EXCEL_FOLDER_PATH) if f.endswith('.xlsx')]
            dataframes = []
            for f in excel_file:
                filepath = os.path.join(self.EXCEL_FOLDER_PATH, f)
                df = pd.read_excel(filepath, dtype = {'Coln A': str, 'column b': str})
                dataframes.append(df)
            kq = pd.concat()
            return kq;
        else:
            print("4756+owkfjnf")
     except Exception as e:
         logging.errors("The path is not available in")
         return pd.DataFrames()

def CapSONhan():
    n =int(input('Nhập số phần tử của dãy: '))
    items = list(map(int, input().split()))
    if len(items) <= 1:
        print("no")
        exit()
    congboi=  items[1] / items[0]
    for i in range(1, n-1):
        if (items[i+1] / items[i] )!= congboi:
            print("Khong phai cap so nhan")
            exit()
    print('La cap so nhan')
    print('Cong boi cua day la: ', congboi)

def CapSocong():
    n =int(input('Nhập số phần tử của dãy: '))
    items = list(map(int, input().split()))
    if len(items) <= 1:
        print("no")
        exit()
    congsai=  items[1] - items[0]
    for i in range(1, n-1):
        if (items[i+1] - items[i] ) != congsai:
            print("Khong phai cap so cong")
            exit()
    print('La cap so cong')
    print('Danh sách: ', items)
    print('Cong boi cua day la: ', congsai)
    print('Tổng các phần tử là: ', sum(items))

def Collatz(x:int):
    return x // 2 if  x % 2 == 0 else 3*x+1

def Print_Collatz(n):
    inc = n
    lst_collatz = []
    if n==1:
        lst_collatz.append(1)
        return lst_collatz
    while inc != 1:
        inc = Collatz(inc)
        lst_collatz.append(inc)
    return lst_collatz

def Main():
    luachon = int(input("Nhap lua chon: "))
    if luachon==1:
        print("Kiem tra cap so nhan")
        CapSONhan()
    if luachon==2:
        print("Kiem tra cap so cong")
        CapSocong()
    if luachon==3:
        print("============================ Collatz number =================================")
        collatz =int(input('Nhập số Collatz: '))
        kq = Print_Collatz(collatz)
        print(kq)


Main()
