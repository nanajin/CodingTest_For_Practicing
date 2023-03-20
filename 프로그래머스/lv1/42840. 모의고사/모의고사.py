def solution(answers):
    answer = []
    cnt1, cnt2, cnt3 = 0,0,0
    spj1 = ([1,2,3,4,5] * len(answers))[0:len(answers)]
    spj2 = ([2,1,2,3,2,4,2,5] * len(answers))[0:len(answers)]
    spj3 = ([3,3,1,1,2,2,4,4,5,5] * len(answers))[0:len(answers)]
    
    for i in range(len(answers)):
        if answers[i] == spj1[i]:
            cnt1 += 1
        if answers[i] == spj2[i]:
            cnt2 += 1
        if answers[i] == spj3[i]:
            cnt3 += 1
    m = max(cnt1, cnt2, cnt3)
    if m == cnt1:
        answer.append(1)
    if m == cnt2:
        answer.append(2)
    if m == cnt3:
        answer.append(3)
    return answer