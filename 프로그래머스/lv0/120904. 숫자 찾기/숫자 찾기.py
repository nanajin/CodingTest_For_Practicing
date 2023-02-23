def solution(num, k):
    num, k = str(num), str(k)
    res = num.find(k)
    if res == -1:
        return res
    else: return res+1
