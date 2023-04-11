def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    l_dic = sorted(dic.items(), key=lambda x: x[1])
    while k > 0:
        k -= l_dic[-1][1]
        l_dic.pop()
        answer += 1
    return answer