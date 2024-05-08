from math import *

def Eratosthenes(n):
    a=[ True for i in range(n+1)]
    for i in range(2, int(sqrt(n))+1):
        if a[i]:
            j=2
            while i*j <= n:
                a[i*j] = False
                j += 1
    return [i for i in range(2, n+1) if a[i]]

print(Eratosthenes(100))