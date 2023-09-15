from math import sqrt, pi
def Main_menu():
    while True:
        print("========================== MENU BAI 2 ===================")
        print("1. Giải phương trình bậc 2")
        print("2. Tính diện tích hình tròn")
        print("3. Đổi giờ - phút - giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây")
        print("4. Mục 1")
        print("5. Tìm số Fibonacci thứ n")
        print("6. Tính n giai thừa")
        print("7. In tam giác vuông")
        print("8. Tinh tong n so Fibonacci dau tien")
        print("9. Xuat cac so nguyen to trong khoang cho truoc")
        print("10. Danh sách số nguyên tố nằm trong khoảng (a,b)")
        print('11. Tính tổng căn bậc 2 của n số nguyên đầu tiên')
        print('12. Kiểm tra số Fibonacci')
        print('13. Câu 12a, 12e, 12h, 12j')
        luachon = int(input("\n Nhập lựa chọn ở đây: "))
        if luachon==1:
            print("{:-^65}".format('PHƯƠNG TRÌNH BẬC HAI'))
            GiaiPTB2()
        elif luachon==2:
            print("{:-^65}".format('DIỆN TÍCH HÌNH TRÒN'))
            DienTichHinhTron()
        elif luachon==3:
            print("{:-^65}".format('ĐỔI GIỜ PHÚT GIÂY'))
            DoiGiay()
        elif luachon==4:    
            print("{:-^65}".format('TỔNG THƯƠNG LŨY THỪA'))
            Cau2_1()
        elif luachon==5:
            print("{:-^65}".format('TÌM SỐ FIBONACCI THỨ N'))
            SoFibo_Thu_n()
        elif luachon==6:
            print("{:-^65}".format('Tính n giai thừa'))
            TinhGiaiThua()
        elif luachon==7:
            print("{:-^65}".format('Tam giác vuông nằm bên trái'))
            TamGiacVuong()
        elif luachon==8:
            print(TongFibonacci())
        elif luachon==9:
            print("{:-^65}" .format("MANG BAN DAU LA"))
            print(my_list)
            print("Các số nguyên tố trong mảng là: ")
            for i in my_list:
                if KTNguyenTo_Mang(i): 
                    print(i, end=' ')
        elif luachon==10: 
            DS_Songuyento_khoang()
        elif luachon==11: TongCanBacHai()
        elif luachon==12:
            number_checkFib =int(input("Nhap so can kiem tra"))
            kq = Check_Fib(number_checkFib)
            print("Fibonacci is correct") if kq else print("Failed!! This is not Fibonacci numbers")
        elif luachon==13: 
            print("{:-^120}".format("-----"))
            DaoNguocChuoi()
            print('\nCâu 12c: Số nguyên tố lớn nhất trong mảng là: ',min_max_prime(my_list))
            Day_Fib()
            TongPTLe()
            TongPTMang()
            SoLanXuatHien()
        else:
            print('\n Please selected from the Menu')
            pass
my_list =[1,-3,-4,5,9,23,4,5,6,0]
def Cau2_1():
    a = int(input('Nhap he so a:'))
    b = int(input('Nhap he so b:'))
    print("Tổng 2 số là: ", a+b)
    if b==0:
        try:
            print("Phép chia {}/{} sai định dạng".format(a,b))
        except:
            print("Không tồn tại kết quả")
    else:
        print("Kết quả {}/{} là:{:.2f} ".format(a,b,a/b))
    print("Kết quả {}^{} là: {} ".format(a,b,a**b))

def TamGiacVuong():
    rows = int(input('Nhập số hàng hoặc cột: '))
    print("\n In * dang tam giac")
    for i in range(1, rows+1):
        for j in range(1, i+1):
            if i==0 or i==rows or j==i or j==1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def DoiGiay():
    so_giay = int(input('Nhập số giây: '))
    so_gio= so_giay % 86400 // 3600
    so_phut=so_giay % 86400 % 3600 // 60
    so_giay = so_giay % 86400 % 3600 % 60
    print(so_gio,":",so_phut,":",so_giay)

def TinhGiaiThua():
    n = int(input('Nhập số cần tính giai thừa: '))
    kq_giaithua=1
    for i in range(1, n+1):
        kq_giaithua=kq_giaithua*i
    print("Kết quả n giai thừa là: ", kq_giaithua)
def DienTichHinhTron():
    Radius = int(input('Nhập bán kính đường tròn: '))
    while Radius<0:
        Radius = int(input('Nhập bán kính đường tròn: '))
        print('Bán kính âm!!! Vu lòng nhập lại: ')
    print("Dien tich hinh tron la: ", pow(Radius,2)*pi)

def Check_Fib(n:int):
    cx = (5*pow(n,2)+4)
    cy = (5*pow(n,2)-4)
    return (sqrt(cx)).is_integer() or sqrt(cy).is_integer()
def Day_Fib():
    for i in range(len(my_list)):
        if Check_Fib(my_list[i]):
            ds = my_list[i]
            print(ds, end=' ')
def TongCanBacHai():
    # O(n)
    n = int(input('Nhap he so can tim:'))
    sum_sqrt=0
    for i in range(1, n+1):
        sum_sqrt += sqrt(i)
    print("Tổng căn bậc 2 của {} số đầu tiên là: {:.2f}".format(n, sum_sqrt))
    return sum_sqrt
    # O(1)
    # return ((n-2)*sqrt(n-1)-2*sqrt(2)+1)*2/3
# return a list of fibonacci numbers
def TongFibonacci():
    n = int(input('Nhap he so can tim:'))
    def fibs(n):
        if n==0: return 0
        elif n == 1: return 1
        else:
            x =[0,1]
            for i in range(n-1):
                x.append(x[-1]+x[-2])
        return x
    def SumFib():
        x = fibs(n)
        sum = 0
        for i in x:
            if i % 2==0: sum+= i
        return sum
    return SumFib()
# def find_smallest_fibonacci(arr)
def SoFibo_Thu_n():
    def Fib_n(fib:int):
        if fib < 3:
            return 1
        return Fib_n(fib -1) + Fib_n(fib - 2)
    fib = int(input('Nhap he so can tim:'))
    print('So fibonacci thu {} la:'.format(fib), Fib_n(fib))

def GiaiPTB2():
    a = int(input('Nhap he so a:'))
    b = int(input('Nhap he so b:'))
    c = int(input('Nhap he so c:'))
    delta = b**2 - 4*a*c
    if a==0:
        print("Phương trình đã trở thành phương trình bậc nhất dạng {}x + {} = 0".format(b,c))
        if b!=0:
            print("Phương trình có nghiệm duy nhất là: ", -c/b)
        else:
            if c==0:
                print('Phương trình có vô số nghiệm ') 
            if c!=0:
                print('Phương trình vô nghiệm ') 
    else:
        if delta >0:
            print("Phuong trinh co hai nghiem phan biet:")
            print("x1 = ", (-b+sqrt(delta)/(2*a)) )
            print("x2 = ", (-b-sqrt(delta)/(2*a)) )
        if delta < 0:
            print('Phương trình vô nghiệm ')
        else:
            print("Phuong trinh co nghiem kep:" , -b/(2*a))

def DS_Songuyento_khoang():
    truoc = int(input('Nhap he so truoc:'))
    sau = int(input('Nhap he so sau:'))
    for num in range(truoc, sau+1):
        coutn=0
        for i in range(2, num//2+1):
            if num%i==0:
                coutn=coutn+1
                break
        if coutn==0 and num!=1:
            print('%d'%num,  end=',')
def KhacHaiVaBa(num:int):
    return num % 2!= 0 and num % 3!= 0

def KhacHaiVaNam(num:int):
    return num % 2 != 0 and num %5 != 0

def Collatz(x:int):
    return x // 2 if  x % 2 == 0 else 3*x+1

def DaoNguocChuoi():
    print("\nCâu 12a: Các số lẻ không chia hết cho 5 là: ", list(filter(KhacHaiVaNam, my_list)))

    list_prime= list(filter(is_prime,my_list))
    print('\nCau 12: Các số nguyên tố trong mảng là: ',list(set(list_prime)))

    list_chiaba = list(filter(KhacHaiVaBa, my_list))
    tich=1
    for i in range(len(list_chiaba)):
        tich *= list_chiaba[i]
    print("\nCâu 12f: Tích các số lẻ không chia hết cho 3 là: {}".format(tich))
    print("\nCâu 12h: Mảng sau khi đảo ngược có dạng: {}".format(list(reversed(my_list))))

    dayle = [i for i in my_list if i % 2!=0]
    daychan = [i for i in my_list if (i%2==0 and i!=0)]
    daychan_le= dayle+ [0]*(my_list.count(0))+ daychan
    print('\nDãy theo kiểu số lẻ xếp trước, chẵn nằm sau, số 0 ở giữa là: {}'.format(daychan_le))
    print('\nCác số Collatz trong dãy gồm: ', list(set(filter(Collatz, my_list))))

def SoLanXuatHien():
    num = int(input("\nNhập phần tử cần kiểm tra: "))
    solan =my_list.count(num)
    print(f'Câu 12k: Phần tử {num} xuất hiện {solan} lần') if solan else print(f'Câu 12k: Phần tử {num} không xuất hiện trong mảng')
def TongPTLe():
    list_khongchiahai = list(filter(lambda x: x% 2 !=0, my_list))
    tong_le =0
    dem =0
    for i in range(0, len(list_khongchiahai)):
        dem +=1
        tong_le+=list_khongchiahai[i]
    print("\nCâu 12e: Trung bình các số lẻ trong danh sách là: {:.2f}".format(tong_le/dem))
# Tính tổng các chữ số của tất cả các số trong danh sách
def TongPTMang():
    tong =0
    for i in range(len(my_list)):
        tong= tong+ my_list[i]
    print("\nCâu 12j: Tổng các phần tử trong mảng là: {}".format(tong))
# Tìm số nguyên tố lơn nhất trong danh sách
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def min_max_prime(arr):
    max_prime = float('-inf')
    for num in arr:
        if is_prime(num):
            max_prime = max(max_prime, num)
    return max_prime
# ================================================
# Tìm phần tử lớn thứ 2 trong danh sách
def KTNguyenTo_Mang(songuyento):
    if songuyento<2: return False
    i = 2
    while songuyento <= i/2:
        if songuyento%i ==0:
            return False
        i+=1    
    return True

Main_menu()
