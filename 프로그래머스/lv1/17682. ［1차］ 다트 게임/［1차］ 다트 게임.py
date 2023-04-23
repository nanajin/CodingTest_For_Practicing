def solution(dartResult):
    res = []
    cnt = -1
    dic = {"S": 1, "D": 2, "T": 3}
    for i in range(1, len(dartResult)):
        if dartResult[i] in dic:
            num = ""
            for j in range(i-1,-1,-1):
                if dartResult[j].isdigit():
                    num += dartResult[j]
                else: break
            num = num[::-1]
            res.append(int(num) ** dic[dartResult[i]])
            cnt += 1
        elif dartResult[i] == "*":
            if cnt == 0:
                res[cnt] *= 2
            else:
                res[cnt] *= 2
                res[cnt-1] *= 2
        elif dartResult[i] == "#":
            res[cnt] *= -1
    return sum(res)