#  hàm trả về list các hệ số tam giác pascal - Không thêm thư viện

def Triangle_Pascal(n:int) -> list:
    list = []
    for i in range(n+1):
        list.append([1 if j in {0,i} else list[i - 1][j - 1] + list[i - 1][j] for j in range(i + 1)])
    return list
x = int(input('Số dòng: '))
for i in Triangle_Pascal(x):
    print(i)