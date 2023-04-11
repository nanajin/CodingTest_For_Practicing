import math
def LCM(n1, n2):
    gcd = math.gcd(n1,n2)
    return n1 // gcd * n2 // gcd * gcd
def solution(arr):
    lcm = LCM(arr[0],arr[1])
    for i in range(2,len(arr)):
        lcm = LCM(lcm, arr[i])
    return lcm