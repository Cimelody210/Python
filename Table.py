from tabulate import tabulate
my_list = [
    ["Python", "Guido van Rossum", 1991],
    ["C", "Dennis Ritchie", 1972],
    ["Java", "James Gosling", 1995],
    ["JavaScript", "Brendan Eich", 1995],
    ["Php", "Rasmus Lerdorf", 1995],
    ["C++", "Bjarne Stroustrup", 1985],
    ["C#", " Anders Hejlsberg", 2000]
]
print(tabulate(my_list, headers=['STT','Ngôn ngữ','Họ và tên','Năm sinh'], showindex='always', numalign='right'))
