def solution(n):
    a, b, cnt = 0,1,1
    while 1:
        if cnt == n:
            break
        a, b = b, a+b
        cnt += 1
    return b % 1234567