def solution(s):
    answer = ''
    res = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    list = sorted(answer)
    for i in list:
        res += i
    return res