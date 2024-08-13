import cv2
import numpy as np

# Đọc ảnh từ file
image = cv2.imread('C:\Users\PC602\Downloads\Lab1\Cau4\Nhận diện ảnh\image_1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Áp dụng GaussianBlur để giảm nhiễu
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# Phát hiện cạnh với Canny
edges = cv2.Canny(blurred, 50, 150)
# Tìm các đường viền (contours) trong ảnh
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)