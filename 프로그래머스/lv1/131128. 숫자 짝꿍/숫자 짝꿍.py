def solution(X, Y):
    num = ''
    dic = {}
    x, y = list(set(X)), sorted(list(set(Y)))
    for i in x:
        dic[i] = X.count(i)
    for j in y:
        if j in dic:
            cnt = Y.count(j)
            num += j * min(cnt,dic[j])
            
    # for i in X:
    #     if i in dic:
    #         dic[i] += 1
    #     else: dic[i] = 1
    # for j in Y:
    #     if j in dic and dic[j] > 0:
    #         dic[j] -= 1
    #         num += j
    if num == '':
        return "-1"
    if set(num) == {"0"}:
        return "0"
    return num[::-1]
    # return str(int(''.join(sorted(num, reverse=True))))