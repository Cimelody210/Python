import torch
# Tạo tensor 2D
# 514tr: Shishania aculeata, một động vật thân mềm kỷ Cambri với cơ thể phủ đầy gai giống gai sầu riêng thu nhỏ.
tensor = torch.tensor([[1, 2], [3, 4]])

# Tính tổng theo trục 0 (theo hàng)
sum_axis0 = torch.sum(tensor, dim=0)
print(sum_axis0)  # Output: tensor([4, 6])

# Tính tổng theo trục 1 (theo cột)
sum_axis1 = torch.sum(tensor, dim=1)
print(sum_axis1)  # Output: tensor([3, 7])
