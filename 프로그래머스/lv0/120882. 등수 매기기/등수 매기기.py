def solution(score):
    answer = []
    dic = {}
    s_score = []
    for i in score:
        avg = (i[0]+i[1])/2
        score[score.index(i)] = avg
    s_score = sorted(score, reverse=True)
    for i in s_score:
        dic[i] = s_score.index(i)+1
    for i in score:
        answer.append(dic[i])
    return answer