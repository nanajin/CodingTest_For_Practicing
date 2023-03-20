def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        s = score[i:i+m]
        if len(s) == m:
            answer += s[-1] * m
    return answer