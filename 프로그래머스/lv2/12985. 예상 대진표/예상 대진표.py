def myNum(num):
    if num % 2 == 0:
        num = num // 2
    else:
        num = num // 2 + 1
    return num
def solution(n,a,b):
    answer = 1
    if myNum(a) == myNum(b):
        return answer
    while 1:
        l = []
        answer += 1
        a = myNum(a)
        b = myNum(b)
        l.append(a)
        l.append(b)
        l.sort()
        if l[0] % 2 != 0:
            if abs(a-b) == 1 or a == b:
                break
    return answer