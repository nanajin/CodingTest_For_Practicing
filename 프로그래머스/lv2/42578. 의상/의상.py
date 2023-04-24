import math
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    
    for k,v in dic.items():
        n = 0
        n += math.comb(v,0) + math.comb(v,1)
        answer *= n
    return answer-1