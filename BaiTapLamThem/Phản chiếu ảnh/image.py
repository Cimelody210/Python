# Cách tạo hình phản chiếu qua gương

from PIL import Image
img = Image.open('Lab2-OOP\TraPhong\Snake.jpg')
phanchieu = img.transpose(Image.FLIP_LEFT_RIGHT)
phanchieu.save(r'Lab2-OOP\TraPhong\result.jpg')
Image.open('Lab2-OOP\TraPhong\result.png')