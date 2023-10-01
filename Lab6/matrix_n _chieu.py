import numpy as np

arr2 = np.array(([(2,4,0,6), (4,7,5,6)],[(0,3,2,1), (9,4,5,6)],[(5,8,6,4), (1,4,6,8)]))

arr_concat = np.array(([(0,-1,-2,-3),(2,-1,-4,-1)]))
print(arr2)
print("Phần tử ở chiều thứ nhất, hàng 1, cột 3 của mảng có giá trị là: ", arr2[1,1,3])
print('Trung bình cộng cua mang la:np.mean(arr2)', arr2.mean())
print('\nTong cua mang la:np.mean(arr2)', arr2.sum())
print('Trung vị của cột đầu tiên là: ',np.median(arr2[:0]))
print('Tổng mỗi hàng là: ', np.sum(arr2, axis=1))
print('\nNorm cấp 2(chiều dài vector) là: ', np.linalg.norm(arr2))
print('GTLN và GTNN cua mang lần lượt là: ', arr2.max(),',',arr2.min())
print('Số phần tử trong mảng là: {}'.format( arr2.size))
print('Số chiều trong mảng là: {}'.format(arr2.ndim))