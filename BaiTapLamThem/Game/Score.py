# bài toán lập lịch thi đấu vòng tròn một lượt cho n đội bóng đá
def generate_schedule(n):
    # Hàm tạo lịch thi đấu cho n đội
    if n == 2:
        return [[1, 2], [2, 1]]

    half = n // 2
    sub_schedule = generate_schedule(half)

    # Khởi tạo lịch thi đấu cho toàn bộ n đội
    schedule = [[0] * (n - 1) for _ in range(n)]

    for i in range(half):
        for j in range(len(sub_schedule[i])):
            if sub_schedule[i][j] != 0:
                # Sao chép lịch thi đấu của các đội từ 1 đến half
                schedule[i][j] = sub_schedule[i][j]
                schedule[i + half][j] = sub_schedule[i][j] + half

                # Cặp đấu giữa các đội trong cùng nhóm
                schedule[i][j] = i + 1
                schedule[i + half][j] = (sub_schedule[i][j] + half - 1) % n + 1

    return schedule

def print_schedule(schedule):
    # Hàm in lịch thi đấu
    n = len(schedule)
    for i in range(n):
        print(" ".join(str(schedule[i][j]) for j in range(len(schedule[i])) if schedule[i][j] != 0))

def main():
    n = int(input("Nhập số đội (n, phải là luỹ thừa của 2): "))

    # Kiểm tra xem n có phải là luỹ thừa của 2 không
    if (n & (n - 1)) != 0:
        print("Số đội phải là luỹ thừa của 2.")
        return

    schedule = generate_schedule(n)
    print_schedule(schedule)

if __name__ == "__main__":
    main()
