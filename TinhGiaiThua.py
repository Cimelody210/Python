def TinhGiaiThua():
    n = int(input('Nhập số cần tính giai thừa: '))
    kq_giaithua=1
    for i in range(1, n+1):
        kq_giaithua=kq_giaithua*i
    print("Kết quả n giai thừa là: ", kq_giaithua)
TinhGiaiThua()
