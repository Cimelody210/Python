# Sau đó  điều chỉnh chỉ số epsilon (e) và minPts (số điểm tối thiểu) với các giá trị khác nhau để quan sát cách các cụm được hình thành.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import NMF
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

cancer = datasets.load_breast_cancer()
X = cancer.data
Y = cancer.target

scaler = StandardScaler()
X_scaler = scaler.fit_transform(X)

dbscan = DBSCAN(eps =2.7, min_samples=5)

labels = dbscan.fit_predict(X_scaler)

pca= PCA(n_components=2)
X_pca = pca.fit_transform(X_scaler)

plt.figure(figsize=(10, 10))

core_example = labels != -1
anomaly = labels == -1

number_of_anomalies = np.sum(labels ==-1)
print('\n Số lượng phần tử dị thường (đám x đỏ) là: '+ str(number_of_anomalies))

plt.scatter(X_pca[core_example, 0], X_pca[core_example,1], c = labels[core_example,], label = 'cluster point')
plt.scatter(X_pca[anomaly, 0], X_pca[anomaly,1], label ='Anomaly', marker='x', color='red')
plt.title('Câu 3: Sử dụng DBSCAN để dò bất thường trên tập dữ liệu Breast Cancer (bệnh nhân ung thư phổi)')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.legend()
plt.show()
