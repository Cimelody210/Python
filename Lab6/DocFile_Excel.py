import pandas as pd
def Main():
    doc_file = pd.read_excel("Lab6\Book.xlsx")
    print(doc_file)
    # Tên của các dòng heading
    print(doc_file.columns.ravel())

    print('\nThống kê số lượng bệnh liên quan đến từng bộ phận trên cơ thể')
    print(doc_file['Loại'].value_counts())
    # In cột thành dict, list
    # print(doc_file['Tên'].to_clipboard())
    # print(doc_file['Tên'].to_list())
    # print(doc_file.to_dict(orient='split'))

    # Convert to csv file
    print(doc_file.to_csv())

    mota = str(input('Nhập mô tả cần tìm: '))
    # mota = sum(doc_file['Nghĩa'].apply(lambda string: mota in string))
    print(mota) if mota else print('Không có miêu tả nào trùng khớp')
    

Main()
