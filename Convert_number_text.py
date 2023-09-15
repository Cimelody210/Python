# Covert number to text

num={1:'Một',2:'Hai', 3:'Ba',4:'Bốn',5:'Năm',6:"sáu",7:'Bảy',8:"tám",9:'Chín',0:"không"}
last  = {1:'Một',2:'Hai', 3:'Ba',4:'Bốn',5:'Năm',6:"sáu",7:'Bảy',8:"tám",9:'Chín',0:""}
classnum = {1:'',2:'mươi',3:'trăm'}
divide = {0:'',1:'nghìn',2:'triệu',3:'tỷ'}

def three(n):
    global last, num, classnum
    out = ' '
    if len(n) ==1:
        return num.get(int(str(n))) + ' '
    elif len(n) ==2 and int(n[0]) ==1:
        if int(n[1] ==1):
            return 'Muoi mot'
        return "Muoi" + last.get(int(n[1]))+' '
    while len(n)> 1:
        if int(str(n)[0]) != 0:
            out += num.get(int(str(n)[0])) +' '+ classnum.get(int(len(str(n)))) +' '
        else:
            out = ' '
        n = str(n[1:])
    return out + last.get(int(n))+ ' '

def Main():
    n = input()
    k1= ''
    max =  len(n) / 3 -0.1
    if len(n) ==1:
        print(num.get(int(n)))
        return
    while len(n) > 1:
        max = int(max)
        if len(n) % 3 == 0:
            k1 += three(n[:3])+ divide.get(max)
            n = n[3:]
        else:
            k1 += three(n[:len(n) % 3])+ divide.get(max)
            n = n[len(n)%3 :]
        max -= 1
    print(k1.strip().replace(' ',' '))
Main()
        