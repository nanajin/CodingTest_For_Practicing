def solution(s):
    l = []
    s = s.split(' ')

    for i in s:
        if i != 'Z': 
            l.append(int(i))
        else:
            l.pop()

    return sum(l)
