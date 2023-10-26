# Trong các năm từ thế kỷ XI đến hết thế kỷ XXI, tìm các năm n thỏa mãn đồng thời các điều kiện sau:
    # Năm nhuận dương lịch (ngày nhuận)
    # Năm nhuận âm lịch (tháng nhuận
    # Năm có 53 tuần (tuần nhuận)
    # Năm có 53 ngày thứ 5 thì được coi là có 53 tuần, tuần thứ 53 được gọi là tuần nhuận.
    # Tổng các chữ số của n là một số nguyên tố.
    # Ví dụ: năm 1024 thỏa mãn đồng thời 4 điều kiện trên.

from calendar import monthrange
from datetime import date
from math import sqrt

def so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def tong(x):
    return sum(int(i) for i in str(x))

def nam_nhuan_d1(n):
    return n % 400 == 0 or (n % 4==0 and n % 100!=0)

def nam_nhuan_al(n):
    return n % 19 in [0,3,6,9,11,14,17]
def tuan_nhuan(y):
    return sum(date(y,m,d).weekday() == 3 \
               for m in range(1, 13)\
                for d in range(1, monthrange(y,m)[1]+1))

for i in range(1001,2101):
    if nam_nhuan_d1(i) and nam_nhuan_al(i) and tuan_nhuan(i) == 53 and so_nguyen_to(tong(i)):
        print(i,end = " ")
