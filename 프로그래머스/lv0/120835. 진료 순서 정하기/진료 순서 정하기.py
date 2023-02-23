def solution(emergency):
    answer = []
    dict = {}
    num = len(emergency)
    s_emer = sorted(emergency)

    for i in s_emer:
        dict[i] = num
        num -= 1
    for j in emergency:
        answer.append(dict[j])
    return answer