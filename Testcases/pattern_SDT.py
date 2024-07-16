import re

text = "Liên hệ: 0987654321 hoặc +84 987 654 321 hay 024-385-1234."

# \b\d{10,11}\b : Số điện thoại Việt Nam 10 hoặc 11 chữ số
#\b(?:\d{2,4}[\s.-]?){2,3}\d{4}\b : Số điện thoại có dấu cách, dấu gạch ngang, hoặc dấu chấm
#\+?84[\s.-]?\d{9,10} :Số điện thoại Việt Nam có mã quốc gia (+84)

# Mẫu regex
pattern = r'\b(?:\d{2,4}[\s.-]?){2,3}\d{4}\b'

phone_numbers = re.findall(pattern, text)
print(phone_numbers)
