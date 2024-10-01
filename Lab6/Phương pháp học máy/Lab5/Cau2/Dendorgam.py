import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

# Tải dữ liệu Wine
wine = datasets.load_wine()
X = wine.data

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaler = scaler.fit_transform(X)

# Sử dụng phương pháp 'ward' để tính toán liên kết phân cấp
link = linkage(X_scaler, method='ward')

# Vẽ dendrogram
plt.figure(figsize=(10, 7))
dendrogram(link, orientation='top', distance_sort='descending', show_leaf_counts=True)

plt.title('Dendrogram for Wine Dataset')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()
