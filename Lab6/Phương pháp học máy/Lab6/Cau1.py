import numpy
from sklearn import linear_model
# Cau 1

# "coefficient" (hệ số) là các giá trị mà mô hình ước lượng để thể hiện mối quan hệ giữa các biến độc lập và biến phụ thuộc nhị phân. 
  # Mỗi hệ số đại diện cho sự thay đổi trong log-odds của biến phụ thuộc khi biến độc lập tương ứng tăng thêm một đơn vị. Log-odds là tỷ lệ giữa xác suất xảy ra của một sự kiện và xác suất không xảy ra.

#  "probability" (xác suất) là xác suất mà một biến phụ thuộc nhị phân (thường là 0 hoặc 1) nhận giá trị 1 (hoặc sự kiện xảy ra) dựa trên các giá trị của các biến độc lập.
  # Xác suất sẽ nằm trong khoảng từ 0 đến 1. Một xác suất gần 1 có nghĩa là sự kiện xảy ra rất có khả năng, trong khi xác suất gần 0 có nghĩa là sự kiện ít có khả năng xảy ra.
  
#Reshaped for Logistic function
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

#predict if tumor is cancerous where the size is 3.46mm
predicted = logr.predict(numpy.array([3.46]).reshape(-1,1))

# Use the function with what we have learned to find out the probability that each tumor is cancerous.
def logit2prob(logr, X):
  log_odds = logr.coef_ * X + logr.intercept_
  odds = numpy.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)

log_odds = logr.coef_
odds = numpy.exp(log_odds)

print(predicted)
print(odds)
print('\n')
print(logit2prob(logr, X))