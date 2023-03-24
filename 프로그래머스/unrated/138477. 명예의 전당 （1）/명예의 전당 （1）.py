def solution(k, score):
    answer = []
    l = []
    for i in range(0,len(score)):
        if i > k:
            if score[i] > l[-1]:
                l.append(score[i])
        else:
            l.append(score[i])
        l.sort(reverse=True)
        l = l[0:k]
        answer.append(l[-1])
    return answer