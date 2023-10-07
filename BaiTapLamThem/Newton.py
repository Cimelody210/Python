# Khai triển nhị thức Newton

def GT(x):
    if x < 2:
        return 1
    return x *GT(x - 1)

# Tổ hợp chập k của n
def C(n, k):
    return GT(n)/(GT(k) * GT(n - k))

to_hop = lambda th: '' if  th == 1 else str(th)

def PhuongTrinh(a, m):
    if m ==0:
        s = ''
    elif m ==1:
        s = a
    else:
        s =  a+ '^' + str(m)
    return s

def NhiThuc_NewTon(a,b,n):
    list = []
    for k in range(n + 1):
        list.append(to_hop(C(n,k))+PhuongTrinh(a, n-k) + PhuongTrinh(b,k))
    string = f"({a} + {b})^{n} = {' + '.join(list)}"
    return string

# Khai triển hằng đẳng thức với  n = 2, 3, 4
print(NhiThuc_NewTon('a','b',2))
print(NhiThuc_NewTon('a','b',3))
print(NhiThuc_NewTon('a','b',4))
