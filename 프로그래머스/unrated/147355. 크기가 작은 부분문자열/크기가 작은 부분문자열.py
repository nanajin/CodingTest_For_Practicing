def solution(t, p):
    answer = 0
    part = []
    for i in range(len(t)):
        s = t[i:i+len(p)]
        if len(s) == len(p):
            part.append(int(s))
    part.sort()
    for i in part:
        if i <= int(p):
            answer += 1
    return answer