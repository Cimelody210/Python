# Câu 1
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Confusion Matrix là một bảng cho thấy số lượng dự đoán đúng và sai của mô hình phân loại, giúp hiểu rõ hơn về cách mà mô hình đang hoạt động.
# Classification Report cung cấp một cái nhìn tổng quan hơn về hiệu suất của mô hình phân loại. Nó thường bao gồm các chỉ số sau:
  # Precision: Tỉ lệ dự đoán đúng trên tổng số dự đoán dương.
  # Recall (Sensitivity): Tỉ lệ dự đoán đúng trên tổng số thực tế dương.
  # F1-score: Trung bình hài hòa của precision và recall.
  # Support: Số lượng mẫu thực tế cho mỗi lớp.

#  F1-micro tính toán tổng số True Positives, False Positives và False Negatives cho tất cả các lớp, sau đó sử dụng các giá trị tổng này để tính precision và recall.
# Nó xem xét tổng thể số lượng mẫu. Nó hữu ích trong các bài toán mà bạn muốn tối ưu hóa tổng số dự đoán đúng cho tất cả các lớp, bất kể kích thước của từng lớp.

# F1-weight tính toán F1-score cho từng lớp nhưng trọng số cho mỗi lớp dựa trên số lượng mẫu của lớp đó.
# Nó cung cấp một cái nhìn tổng thể mà vẫn cân nhắc đến sự phân bổ mẫu giữa các lớp. Điều này hữu ích trong các bài toán mà các lớp không được phân bổ đều, giúp cải thiện khả năng phản ánh thực tế của mô hình.

# Tải tập dữ liệu Iris
iris = datasets.load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=40)

# Khởi tạo và huấn luyện mô hình Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, Y_train)

Y_pred = gnb.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
conf_matrix = confusion_matrix(Y_test, Y_pred)
classi_report = classification_report(Y_test, Y_pred)

# In kết quả
print(f"Accuracy: {accuracy:.3f}")
print("Confusion matrix:")
print(conf_matrix)
print("Classification report:")
print(classi_report)
