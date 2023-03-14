def solution(n):
    a = n ** 0.5
    if str(a)[-1] == '0':
        return (int(a)+1)**2
    return -1