from itertools import *
def sosu(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    c_list = list(combinations(nums,3))
    for i in c_list:
        if sosu(sum(i)):
            answer += 1
    return answer