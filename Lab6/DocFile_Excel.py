import pandas as pd
def Main():
    doc_file = pd.read_excel("Lab6\Book.xlsx")
    print(doc_file)

    print('\nThống kê số lượng bệnh liên quan đến từng bộ phận trên cơ thể')
    print(doc_file['Loại'].value_counts())

    mota = str(input('Nhập mô tả cần tìm: '))
    Saturn = sum(doc_file['Mô tả(nếu có)'].apply(lambda string: mota in string))
    print(Saturn) if Saturn else print('Không có vật thể nào')
    

Main()
