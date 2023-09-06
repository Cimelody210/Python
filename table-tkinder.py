from tkinter import *
from  tkinter import ttk

ws  = Tk()
ws.title('Wanted Criminal List')
ws.geometry('500x500')
ws['bg'] = 'cyan'

game = Frame(ws)
game.pack()

Scroll = Scrollbar(game)
Scroll.pack(side=RIGHT, fill=Y)
Scroll = Scrollbar(game, orient='horizontal')
Scroll.pack(side=BOTTOM, fill=X)

member = ttk.Treeview(game, yscrollcommand = Scroll.set, xscrollcommand = Scroll.set)
game.pack()

Scroll.config(command=game.winfo_y)
Scroll.config(command=game.winfo_x)

member['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

member.column("#0", width=0,  stretch=NO)
member.column("player_id",anchor=CENTER, width=80)
member.column("player_name",anchor=CENTER,width=80)
member.column("player_Rank",anchor=CENTER,width=80)
member.column("player_states",anchor=CENTER,width=80)
member.column("player_city",anchor=CENTER,width=80)

member.heading("#0",text="",anchor=CENTER)
member.heading("player_id",text="Id",anchor=CENTER)
member.heading("player_name",text="Name",anchor=CENTER)
member.heading("player_Rank",text="Rank",anchor=CENTER)
member.heading("player_states",text="States",anchor=CENTER)
member.heading("player_city",text="City",anchor=CENTER)

member.insert(parent='',index='end',iid=0,text='', values=('1','Li Zuocheng','101','Beijing', 'China'))
member.insert(parent='',index='end',iid=1,text='', values=('2','Zhang Youxia','102','beijing', 'China'))
member.insert(parent='',index='end',iid=2,text='', values=('3','Nina Blamer','103', 'Hamburg', 'Germany'))
member.insert(parent='',index='end',iid=3,text='', values=('4','Dragon','104','New York' , 'White Plains'))
member.insert(parent='',index='end',iid=4,text='', values=('5','CrissCross','105','California', 'San Diego'))
member.insert(parent='',index='end',iid=5,text='', values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
member.insert(parent='',index='end',iid=6,text='', values=('7','ZaqueriBlack','106','Wisconsin' , 'TONY'))
member.insert(parent='',index='end',iid=7,text='', values=('8','ZaqueriBlack','106','Wisconsin' , 'TONY'))
member.insert(parent='',index='end',iid=8,text='', values=('9','ZaqueriBlack','106','Wisconsin' , 'TONY'))
member.insert(parent='',index='end',iid=9,text='', values=('10','ZaqueriBlack','106','Wisconsin' , 'TONY'))
member.insert(parent='',index='end',iid=10,text='', values=('11','ZaqueriBlack','106','Wisconsin' , 'TONY'))
member.insert(parent='',index='end',iid=11,text='', values=('12','ZaqueriBlack','106','Wisconsin' , 'TONY'))
member.insert(parent='',index='end',iid=12,text='', values=('13','ZaqueriBlack','106','Wisconsin' , 'TONY'))

member.pack()
frame = Frame(ws)
frame.pack(pady=20)
# Label
LabelsID = Label(frame, text="player_id")
LabelsID.grid(row=0, column=0)
LabelName = Label(frame, text='player_name')
LabelName.grid( row=0, column=1)
LabelRank = Label(frame, text='player_Rank')
LabelRank.grid( row=0, column=2)
# Entry
Entry_ID = Entry(frame)
Entry_ID.grid( row=1, column=0)
Entry_Name = Entry(frame)
Entry_Name.grid(row=1, column=1)
Entry_Rank= Entry(frame)
Entry_Rank.grid( row=1, column=2)
def Select():
    Entry_ID.delete(0, END)
    Entry_Name.delete(0, END)
    Entry_Rank.delete(0, END)

    selected =  game.focus()
    values = game.item(selected,'values')

    Entry_ID.insert(0, values[0])
    Entry_Name.insert(0, values[1])
    Entry_Rank.insert(0, values[2])
def Save():
    selected  = game.focus()
    game.item(selected,text="",values=(Entry_Name.get(),Entry_Name.get(),Entry_Rank.get()))
    Entry_ID.delete(0, END)
    Entry_Name.delete(0, END)
    Entry_Rank.delete(0, END)

select_btn = Button(ws, text="Select record", command=Select)
select_btn.pack(pady=10)
refresh_btn = Button(ws, text="Refresh record", command=Save)
refresh_btn.pack(pady=10)
temp_label = Label(ws, text='')
temp_label.pack()

ws.mainloop()
