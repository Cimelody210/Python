print('''
    Set trong python là một tập các giá trị không có thứ tự. Mỗi giá trị trong set là duy nhất, không thể lặp lại và bất biến( tức bạn không thể thay đổi giá trị các phần tử trong set).
    Tuy nhiên các set có thể thay đổi. Chúng ta có thể thêm, xóa các phần tử trong set.
    Các set  có thể được sử dụng để thực hiện các phép tập hợp như phép giao, hợp, …''')
# impermance of life after fire mini apartment in Hanoi
# (Cuộc sống vô thường)
my_list =[1,-3,-4,5,9,23,4,1, 2, 4, 6 ,4,4,-10,3,-1,-1]
update_lst = ['Starting','For','IELTS']
kq = set(my_list)

def main():
    print('''
    ====================== KIỂU DỮ LIỆU SET TRONG PYTHON =============
    1. Thêm phần tử vào trong set
    2. Cập nhật set: 
    3. Xóa  một phần tử trong set
    4. Xóa nhiều phần tử trong set
    5. Pop trong set    
    ''')
    n = int(input('Nhap lua chon: '))
    if n==1:
        items = input('Thêm phần tử vào trong set: ')
        print("Kết quả ban đầu: ", kq)
        kq.add(items)
        print("Kết quả sau khi thêm: ", kq)
    elif n==2:
        print(kq)
        kq.update(update_lst)
        print(f"Set mới sau khi update thêm list {update_lst}: ")
        print(kq)
    elif n==3:
        items = int(input('Nhập phần tử muốn xóa khỏi set: '))
        kq.remove(items)
        print(kq)
    elif n==4:
        print(kq)
        for items in range(2,6):
            # kq.discard(items)
            kq.remove(items)
        print(kq)
    elif n==5:
        print(kq)
        kq.pop()
        print(kq)

main()