import random as rd

def is_HV(n):
    sq  = n**0.5
    return int(sq) == sq

nums= rd.sample(range(10**2, 10**3+1), k=10)
print(nums)
print(sum(1 for x in nums if is_HV(x)))