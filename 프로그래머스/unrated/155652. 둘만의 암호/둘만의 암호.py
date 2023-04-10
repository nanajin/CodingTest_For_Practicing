def solution(s, skip, index):
    answer = ''
    idx = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alpha = alpha.replace(i,"")

    for i in s:
        idx = alpha.index(i)+index
        while idx >= len(alpha):
            idx -= len(alpha) 
        answer += alpha[idx]
    return answer