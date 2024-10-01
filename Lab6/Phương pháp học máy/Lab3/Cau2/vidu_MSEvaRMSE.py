# MAE là trung bình cộng của các giá trị tuyệt đối của lỗi giữa các giá trị dự đoán và giá trị thực tế.
# RMSE là căn bậc hai của trung bình cộng các bình phương của lỗi giữa các giá trị dự đoán và giá trị thực tế.

# R^2 là tỷ lệ giữa tổng phương sai của dự đoán và tổng phương sai của giá trị thực tế. Nó thể hiện mức độ biến thiên của giá trị thực tế được mô hình giải thích.
    # Công thức: R^2 =  1 - (RSS / TSS)
    # Với RSS  = Tổng của các bình phuong lỗi và RSS: Tổng các bình phương tổng quát
    # R^2 = 1: Mô hình giải thích hoàn toàn biến thiên của dữ liệu. Dự đoán hoàn toàn khớp với giá trị thực tế.
    # R^2 =0: Mô hình không giải thích được bất kỳ biến thiên nào ngoài giá trị trung bình của dữ liệu. Mô hình không tốt hơn một dự đoán ngẫu nhiên dựa trên trung bình của dữ liệu.
    # R^2 <0: Mô hình kém hơn một mô hình mà chỉ dự đoán giá trị trung bình của dữ liệu. Điều này thường xảy ra khi mô hình không phù hợp hoặc rất kém.

    # Vd: Nếu R^2 = 0.65. Điều này có nghĩa là mô hình của bạn giải thích 65% biến động trong dữ liệu phụ thuộc. Phần còn lại 35% biến động

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Giá trị thực tế và các giá trị dự đoán
y_true = np.array([120, 100, 60, 40])
y_pred = np.array([19, 43, 56, 26])


mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
r2 = r2_score(y_true, y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f'Gia tri cua R2 la: {r2}')


