# hiển thị tất cả ngày thứ Sáu trong năm 2014. Biết rằng thứ ssáu đầu tiên ngày 3/1

def is_leap_year(year):
  return (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0)
def get_days (month, year):
  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if is_leap_year (year):
    days [1] = 29
  
  return days [month-1]

fri = 3
year = 2014
print(fri)
for month in range(1, 13):
  days = get_days (month, year)
  while fri + 7 <= days:
    fri += 7
    print(fri)
  if month != 12:
    fri = (fri + 7) - days
    print(fri)