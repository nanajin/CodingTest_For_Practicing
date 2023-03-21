import math
def lcm(n,m,l):
    gcd = math.gcd(n,m)
    a = 1
    if gcd == 1:
        for i in l:
            a *= i
        return n*m*a
    n //= gcd
    m //= gcd
    l.append(gcd)
    return lcm(n,m,l)
def solution(n, m):
    answer = []
    return [math.gcd(n,m), lcm(n,m,[])]