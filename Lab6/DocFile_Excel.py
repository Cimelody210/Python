import pandas as pd
def Main():
    doc_file = pd.read_excel("Lab6\Book.xlsx")
    print(doc_file)

    print('\nThống kê số lượng bệnh liên quan đến từng bộ phận trên cơ thể')
    print(doc_file['Loại'].value_counts())

    mota = str(input('Nhập mô tả cần tìm: '))
    mota = sum(doc_file['Nghĩa'].apply(lambda string: mota in string))
    print(mota) if mota else print('Không có miêu tả nào trùng khớp')


Main()
