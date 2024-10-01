import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filename = "C:\Users\PC602\Downloads\Lab2\Cau2\data.csv"

df = pd.read_csv(filename)

print("Cau 1")
print(df)

print("\n")
print("Cau 2")
print("Thông tin dataframe:")
print(df.info())

print("\nXem thông tin 3 dòng đầu tiên")
print(df.head(3))

print("\nXem thông tin 3 dòng cuối cùng")
print(df.tail(3))

print("\nXem thông tin dòng thứ 5")
print(df.iloc[5])

print("\n Xem thông tin dữ liệu null")
print(df.isnull())

print("\n Xem độ tương đồng giữa các dữ liệu")
tuongdong = df.corr()
print(tuongdong)
    # heigh    weight       bmi
    # heigh   1.000000  0.630767  0.273934
    # weight  0.630767  1.000000  0.917363
    # bmi     0.273934  0.917363  1.000000

print("\n Xem thông tin mo ta dữ liệu")
print(df.describe())
print("Cau 3")

plt.figure(dpi = 300)
sns.heatmap(tuongdong, annot=True, fmt='.lf')
plt.show()

dropna = df.dropna(inplace = True)
dropna = df[(df >= 0).all(axis=1)]

df.to_csv('cleaned_data.csv', index=False, sep='\t')



