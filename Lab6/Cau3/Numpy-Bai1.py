import pandas as pd

data= pd.read_csv('Lab1\Cau3\Automobile_data.csv')

print(data.head(3))
print('\nXuất thông tin của dữ liệu như sau:')
# print(data.info())

company =    data.groupby('company')
Toyota_data = company.get_group('toyota')
average_price_car = company[['company','price']].mean('price')

print(Toyota_data)

print('\nĐếm số xe của từng hãng')
print(data['company'].value_counts())

print('\nHiển thị giá xe trung bình của mỗi hãng xe')
print(average_price_car)

print('\nHiển thị giá xe cao nhất của mỗi hãng xe')