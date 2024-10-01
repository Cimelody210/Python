import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, SparsePCA

# Tạo dữ liệu giả lập
X = np.array([[1.0, 2.0, 3.0],
              [2.0, 3.0, 4.0],
              [3.0, 4.0, 5.0],
              [4.0, 5.0, 6.0]])

# Thực hiện PCA thông thường
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("PCA components:")
print(pca.components_)

# Thực hiện SparsePCA
sparse_pca = SparsePCA(n_components=2, alpha=1)  # alpha điều chỉnh độ thưa thớt
X_sparse_pca = sparse_pca.fit_transform(X)

print("\nSparsePCA components:")
print(sparse_pca.components_)

# Vẽ đồ thị các thành phần chính
plt.figure(figsize=(10,5))

# PCA thông thường
plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='b', label='PCA')
plt.title('PCA')
plt.xlabel('Component 1')
plt.ylabel('Component 2')

# SparsePCA
plt.subplot(1, 2, 2)
plt.scatter(X_sparse_pca[:, 0], X_sparse_pca[:, 1], c='r', label='SparsePCA')
plt.title('SparsePCA')
plt.xlabel('Component 1')
plt.ylabel('Component 2')

plt.tight_layout()
plt.show()
