def solution(n):
    answer = 0
    one = bin(n)[2:].count("1")
    i = 1
    while 1:
        if bin(n+i)[2:].count("1") == one:
            answer = n+i
            break
        i += 1
    return answer