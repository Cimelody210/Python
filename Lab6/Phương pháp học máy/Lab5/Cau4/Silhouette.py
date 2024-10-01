import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Tạo dữ liệu mẫu
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

kmeans = KMeans(n_clusters=4)
y_kmeans = kmeans.fit_predict(X)

# Tính chỉ số Silhouette
silhouette_avg = silhouette_score(X, y_kmeans)
print('''
  Công thức tính:
    s(i) = ( b(i) - a(i) ) / ( max( a(i), b(i)) )
    s(i) = 0 thì không thể xác định được i nên thuộc về cụm nào
    s(i) càng gần -1 thì chứng tỏ i bị phân sai cụm, nó nên thuộc về cụm hàng xóm chứ không phải cụm hiện tại.
''')
print('Chỉ số này cho biết độ tương đồng giữa các điểm trong cùng cụm so với các cụm khác. Giá trị càng cao (tối đa 1) cho thấy phân cụm tốt hơn.')
print(f"Chỉ số Silhouette: {silhouette_avg:.5f}")

# Vẽ dữ liệu và cụm
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# Vẽ trung tâm của các cụm
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=120, alpha=0.75, marker='X')
plt.title('Phân cụm KMeans với Silhouette Score')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')
plt.show()
