from tkinter import *
from tkinter import ttk, messagebox

SV_form = Tk()
SV_form.geometry('700x400')
SV_form.title('Dang ky hoc phan')
SV_form.configure(background = "light green")

def InputError():
    if input_mssv.get() == '' and ValueError(input_mssv) and len(input_mssv)>8:
        messagebox.showerror('Sai MSSV')
        return 0
    if ValueError(input_hoten) and input_hoten.get()=='':
        messagebox.showerror('Sai tên')
        return 0
    if ValueError(input_sdt) and len(input_sdt) >10:
        messagebox.showerror('Sai số điện thoại')
        return 0
    hk =[1,2,3]
    if ValueError(input_hk) and input_hk != hk:
        messagebox.showerror('Học kỳ chỉ được chọn 1,2 hoặc 3')
        return 0
    return 1


def btn_DangKy_Click():
    global click
    giatri = InputError()
    if giatri ==0:
        return
    
DSMH = Canvas(SV_form, width = 400)
DSMH.create_rectangle(20,8,382,200, outline='light green')
DSMH.configure(background='light green')
DSMH.grid(row=8, column=1)

# img =  PhotoImage(file= r'\Lab4\3135715.png')
none = Label(SV_form, text='')
none.configure(background='light green')
none.grid(row=0, column=0)


TITLE = Label(SV_form, text='THONG TIN DANG KY HOC PHAN', fg='red', font='24px')
TITLE.configure(background='light green')
TITLE.grid(row=0, column=1)

MSSV = Label(SV_form, text = "Mã số sinh viên", padx=30)
MSSV.configure(background='light green')
MSSV.grid(row=1, column=0)
input_mssv = Entry(width=60)
input_mssv.grid(row=1, column=1)

HoTen = Label(SV_form, text = "Họ và tên", padx=10)
HoTen.grid(row=2, column=0)
HoTen.configure(background='light green')
input_hoten = Entry(width=60)
input_hoten.grid(row=2, column=1)

NgaySinh = Label(SV_form, text = "Ngày sinh")
NgaySinh.configure(background='light green')
NgaySinh.grid(row=3, column=0)

input_ngaysinh = Entry(width=60)
input_ngaysinh.grid(row=3, column=1)

Email = Label(SV_form, text = "Email")
Email.configure(background='light green')


input_Email =  Entry(width=60)
Email.grid(row=4, column=0)
input_Email.grid(row=4, column=1)

SDT = Label(SV_form, text = "Số điện thoại")
SDT.configure(background='light green')
input_sdt = Entry(width=60)
SDT.grid(row=5, column=0)
input_sdt.grid(row=5, column=1)

HK = Label(SV_form, text = "Học kỳ")
HK.configure(background='light green')
input_hk = Entry(width=60)
HK.grid(row=6, column=0)
input_hk.grid(row=6, column=1)

NamHoc = Label(SV_form, text = "Năm học")
NamHoc.configure(background='light green')
NamHoc.grid(row=7, column=0)

cbo_namhoc = Label(SV_form, text = "Chọn môn học")
cbo_namhoc.configure(background='light green')
cbo_namhoc.grid(row=8 , column=0)
cbo_namhoc.place(x=30, y=180)

n = StringVar()
MH_list = ttk.Combobox(SV_form, width =57,textvariable = n)
MH_list['values'] = ('2022-2023', '2023-2024', '2024-2025')
MH_list.grid(row=7, column=1)
MH_list.current(0)

checkbtn_python =  Checkbutton(SV_form, text='Lập trình Python')
checkbtn_python.configure(background='light green')
checkbtn_CNPM =  Checkbutton(SV_form, text='Công nghệ phần mềm')
checkbtn_CNPM.configure(background='light green')
checkbtn_java =  Checkbutton(SV_form, text='Lập trình Java')
checkbtn_java.configure(background='light green')
checkbtn_PTUDWeb =  Checkbutton(SV_form, text='Phát triển ứng dụng web')
checkbtn_PTUDWeb.configure(background='light green')
checkbtn_UIUX =  Checkbutton(SV_form, text='Thiết kế giao diện')
checkbtn_UIUX.configure(background='light green')
checkbtn_CSharp =  Checkbutton(SV_form, text='Lập trình C#')
checkbtn_CSharp.configure(background='light green')
btn_Thoat =  Button(SV_form, text='Thoát', bg='green', width=12, fg="white", command=SV_form.destroy)
btn_DangKy = Button(SV_form, text='Đăng ký', bg='green', width=12, fg="white", command=btn_DangKy_Click)

checkbtn_python.place(x=170,y=190)
checkbtn_CNPM.place(x=170,y=230)
checkbtn_PTUDWeb.place(x=350, y=230)
checkbtn_UIUX.place(x=170, y=270)
checkbtn_java.place(x=350, y=190)
checkbtn_CSharp.place(x=350, y=270)
btn_DangKy.place(x=200, y=310)
btn_Thoat.place(x=350, y=310)

# TITLE.pack(side=TOP)

SV_form.mainloop()