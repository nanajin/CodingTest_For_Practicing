def solution(n):
    if n < 3:
        return n
    l = [0] * n
    l[0], l[1] = 1, 2
    
    for i in range(2, n):
        l[i] = l[i-1] + l[i-2]
    return l[-1] % 1234567