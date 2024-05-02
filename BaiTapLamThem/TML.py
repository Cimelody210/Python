import random
ocean = [['~' for _ in range(3)] for _ in range(3)]
treasue_row, treasure_col = random.randint(0,2), random.randint(0,2)

def MSG():
    print('aaaaa')
    print('aaaaa')
    print('aaaaa')
    input()
    print('aaaaa')
    input()
def in_ocean(ocean):
    for row in ocean:
        print(' '.join(row))
    print()
def KT_KhoBau(row, col):
    if row == treasue_row and col == treasure_col:
        ocean[row][col] = 'T'
        in_ocean(ocean)
        print('May da tim dc kho bau cua tao')
        return True
    else:
        ocean[row][col] = 'x'
        print('May con non va xanh lam con a')
        return False


def game():
    MSG()
    while True:
        in_ocean(ocean)
        row, col = map(int, input("Nhap toa do cua thuyen truong").split())
        if row ,0 or row >2  or col < 0 or col > 2:
            print("Toa do sai, nhap tu 0-2")
            continue
        if ocean[row][col] =="X":
            print("may da qua cho nay r, tim cho khac nhe")
            continue
        if KT_KhoBau(root, col):
            break;
game()

        