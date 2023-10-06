import pandas as pd

# Sử dụng pandas đọc tập tin dữ liệu sales_data.csv và thực hiện các yêu cầu sau:


def Main():
    doc_file = pd.read_csv("Lab6\sales_data.csv")
    print('\n1. Hiển thị nội dung toàn bộ dữ liệu')
    print(doc_file)

    print('\n2. Dữ liệu này có bao nhiêu cột, tên của các cột là')
    print(doc_file.info())

    print('\n3. Dữ liệu của tháng có lợi nhuận cao nhất : ')
    loinhuan = pd.DataFrame(doc_file['total_profit'])
    print(loinhuan.max())

    print('\n4. Xuất hàng dữ liệu của tháng bán nhiều mặt hàng nhất')
    max_units = pd.DataFrame(doc_file['total_units'])
    print(max_units.max())

    print('\n5. Xuất hàng dữ liệu của tháng bán nhiều kem đánh răng nhất ')
    kemdanhrang = pd.DataFrame(doc_file['toothpaste'])
    print(kemdanhrang.max())
    

    print('\n6. Lợi nhuận của năm là: ')
    tong_donvi = pd.DataFrame(doc_file['total_units'])
    tong_giaca = pd.DataFrame(doc_file['total_profit'])

    print(tong_giaca)
    # tong_donvi = tong_donvi.sum()
    # tong_giaca =  tong_giaca.sum()
    # print(tong_donvi* tong_giaca)
    

    print('\n7. Cho biết tổng số lượng đã bán theo mặt hàng: ')
    facecream = pd.DataFrame(doc_file['facecream'])
    facewash = pd.DataFrame(doc_file['facewash'])
    toothpaste = pd.DataFrame(doc_file['toothpaste'])
    print(facecream.sum())
    print(facewash.sum())
    print(toothpaste.sum())

    print('\n8. Hiển thị số lượng các mặt hàng bán trong tháng 2 ')
    thang2 = pd.DataFrame(doc_file[doc_file['month_number'] == 2])
    thang2 = thang2.drop('total_profit', axis=1)
    thang2 = thang2.drop('total_units', axis=1)
    print(thang2)
    print('Số lượng mặt hàng bán chạy nhất tháng 2: ')
    print(thang2.max(axis=1))
    

    print('\n9. Số lượng mặt hàng bán chạy nhất tháng 2  ')
    
Main()
