def change_number(num):
    n = ''
    while num > 0:
        n += str(num % 3)
        num = num // 3
    return n
def solution(n):
    return int(change_number(n),3)