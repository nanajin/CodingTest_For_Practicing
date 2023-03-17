def solution(survey, choices):
    answer = ''
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0,}
    score_dic = {'1': 3, '2': 2, '3': 1, '4': 0, '5': 1, '6': 2, '7': 3}
    group = ['RT', 'CF', 'JM', 'AN']
    for i in range(len(survey)):
        agree, disagree = 0, 0
        if choices[i] in [5, 6, 7]:
            agree += score_dic[str(choices[i])]
        else:
            disagree += score_dic[str(choices[i])]
        
        dic[survey[i][0]] += disagree
        dic[survey[i][1]] += agree

    for i in group:
        if dic[i[0]] > dic[i[1]] or dic[i[0]] == dic[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer