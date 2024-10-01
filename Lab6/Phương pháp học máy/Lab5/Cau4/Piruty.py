# Thang đo Purity cho các bài toán phân cụm. 

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Tạo dữ liệu mẫu với các cụm thực tế
X, y_true = make_blobs(n_samples=500, centers=4, cluster_std=0.35, random_state=0)

# Thực hiện phân cụm bằng KMeans với 4 cụm
kmeans = KMeans(n_clusters=4, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Hàm tính Purity
def purity_score(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    # Tính purity bằng cách lấy nhãn đúng nhất trong mỗi cụm
    return np.sum(np.amax(matrix, axis=0)) / np.sum(matrix)

# Tính Purity
purity = purity_score(y_true, y_kmeans)

# Vẽ dữ liệu và phân cụm
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.title('KMeans Clustering Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster Label')
plt.grid()

# Hiển thị ma trận nhầm lẫn
plt.figure(figsize=(10, 6))
conf_matrix = confusion_matrix(y_true, y_kmeans)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y_kmeans), yticklabels=np.unique(y_true))
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()