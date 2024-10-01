from sklearn.decomposition import TruncatedSVD
import numpy as np
import pandas as pd

# Tạo một bộ dữ liệu số giả lập
data = np.array([
    [1, 0, 0, 4],
    [2, 0, 1, 3],
    [3, 1, 0, 2],
    [4, 0, 0, 1],
    [5, 0, 1, 0]
])

# Tạo DataFrame để dễ quan sát
df = pd.DataFrame(data, columns=['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'])

# In dữ liệu ban đầu
print("Dữ liệu gốc:")
print(df)

# Áp dụng TruncatedSVD để giảm chiều
n_components = 2  # Số lượng thành phần giữ lại
svd = TruncatedSVD(n_components=n_components)
data_reduced = svd.fit_transform(data)

# Kết quả sau khi giảm chiều
print(f"\nOriginal shape: {data.shape}")
print(f"Reduced shape: {data_reduced.shape}")
print(pd.DataFrame(data_reduced, columns=[f"Component {i+1}" for i in range(n_components)]))
