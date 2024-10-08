import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage


data = '/content/Cau3/weatherAUS.csv'

read = pd.read_csv(data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
chiadulieu = pd.get_dummies(read.WindDir3pm, drop_first=True, dummy_na=True).head()

categorical = [var for var in read.columns if read[var].dtype=='O']

print('The categorical variables are :', categorical)
print("Shape of X_train is ", X_train.shape)
# print(read.head(6))
# print(read.shape)
# print(read)
# print(read.columns)
# print(read.info())
# print(read.drop(['WindGustDir'], axis=1, inplace=True))
# print('There are {} categorical variables\n'.format(len(categorical)))
# print(read.Location.value_counts())

plt.figure(figsize=(15,10))
# Tạo các boxplot
plt.subplot(2, 2, 1)
fig1 = read.boxplot(column='Rainfall')
fig1.set_title('Boxplot of Rainfall')
fig1.set_ylabel('Rainfall')

plt.subplot(2, 2, 2)
fig2 = read.boxplot(column='Evaporation')
fig2.set_title('Boxplot of Evaporation')
fig2.set_ylabel('Evaporation')

plt.subplot(2, 2, 3)
fig3 = read.boxplot(column='WindSpeed9am')
fig3.set_title('Boxplot of Wind Speed at 9am')
fig3.set_ylabel('Wind Speed (9am)')

plt.subplot(2, 2, 4)
fig4 = read.boxplot(column='WindSpeed3pm')
fig4.set_title('Boxplot of Wind Speed at 3pm')
fig4.set_ylabel('Wind Speed (3pm)')

# Tách riêng các histogram
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
luongmua1 = read.Rainfall.hist(bins=10)
plt.xlabel('Rainfall')
plt.ylabel('Frequency')
plt.title('Histogram of Rainfall')

plt.subplot(2, 2, 2)
luongmua2 = read.Evaporation.hist(bins=10)
plt.xlabel('Evaporation')
plt.ylabel('Frequency')
plt.title('Histogram of Evaporation')

plt.subplot(2, 2, 3)
luongmua3 = read.WindSpeed9am.hist(bins=10)
plt.xlabel('WindSpeed9am')
plt.ylabel('Frequency')
plt.title('Histogram of Wind Speed at 9am')

plt.subplot(2, 2, 4)
luongmua4 = read.WindSpeed3pm.hist(bins=10)
plt.xlabel('WindSpeed3pm')
plt.ylabel('Frequency')
plt.title('Histogram of Wind Speed at 3pm')

plt.tight_layout()  # Tự động điều chỉnh khoảng cách giữa các đồ thị
plt.legend()
plt.show()