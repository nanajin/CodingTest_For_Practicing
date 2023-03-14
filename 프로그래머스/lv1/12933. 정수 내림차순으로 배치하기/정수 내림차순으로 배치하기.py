def solution(n):
    answer = ''
    l = sorted([i for i in str(n)], reverse=True)
    for i in l:
        answer += i
    return int(answer)