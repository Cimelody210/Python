n=int(input('Nhap so: '))
while n<=0:
    print("Nhap sai: Nhap lai: ")
    n=int(input('Nhap so nguyen duong: '))
def Tong_N_So():
    sum=0
    for i in range(0,n+1):
        sum+=i
    print("Ket qua cua {} so nguyen dau la: {}".format(n, sum))
Tong_N_So()
