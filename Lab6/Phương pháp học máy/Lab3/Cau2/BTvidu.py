# MAE là trung bình cộng của các giá trị tuyệt đối của lỗi giữa các giá trị dự đoán và giá trị thực tế.
# RMSE là căn bậc hai của trung bình cộng các bình phương của lỗi giữa các giá trị dự đoán và giá trị thực tế.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
Y = np.array([3,4,2,5,7,8,8,9,10,12])

X_train,Y_train, y_test, x_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, Y_train)
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.scatter(X,Y, color = 'green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('shfhgherghe')
plt.show()
