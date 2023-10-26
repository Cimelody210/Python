# Duyệt web trong pytohn
import webbrowser as web
s= 'Thanh nien, Vn Express'
url = ['https://vnexpress.net/','https://thanhnien.vn/']
print(s)
t1 = "C"
while t1.upper() == "C":
    i = int(input('Bạn muốn xem tin tức từ trang nào (1/2/3/4/5)?'))
    web.open_new_tab(url[i-1])
    tl = input('Tiếp tục hay không (C/K)?')