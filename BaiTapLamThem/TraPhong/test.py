def main():
    
    gia_1_dem= {1:1260,2:1550, 3:1830,4:1830, 5:2120, 6:2120, 7:2540, 8:4800}
    room_type = int(input(' Nhap loai phong(tu 1-8)'))
    day = int(input(' Nhap so dem)'))
    day = int(input(' Nhap so dem)'))    # Lúc tạo dict giá 1 đêm,đơn vị tính là ngàn đồng => khi tính thành tiền, nhân với 10^3 để về đơn vị tính là đ.
    price=  gia_1_dem[room_type] * 10 **3
    if day== 2 and day==3:
        price *= 0.75*day
    elif day >3:
        price *= 0.7*day
    print(price)
main()