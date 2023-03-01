import math
def insu(num):
    i = 2
    insu_list = []
    while num > 1:
        if num % i == 0:
            if i not in insu_list:
                insu_list.append(i)
            num = num // i
        else:
            i += 1
    return insu_list
def solution(a, b):
    gcd = math.gcd(a,b)
    b = b // gcd
    i_list = insu(b)
    length = len(i_list)
    if length == 0:
        return 1
    elif length <= 2:
        if i_list.count(2) + i_list.count(5) == length:
            return 1
    return 2