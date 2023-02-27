def solution(i, j, k):
    answer = 0
    for w in range(i,j+1):
        w, k = str(w), str(k)
        if k in w:
            answer += w.count(k)
    return answer