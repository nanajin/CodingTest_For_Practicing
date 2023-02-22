def solution(n):
    answer = 0
    i = 1
    while 1:
        value = (n * i) // 6
        if (n * i) % 6 == 0:
            return value
            break
        else:
            i += 1