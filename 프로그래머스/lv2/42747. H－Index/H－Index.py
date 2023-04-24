def solution(citations):
    citations.sort()
    h = 0
    l = []
    while h < citations[-1]:
        cnt = 0
        for i in citations:
            if i >= h:
                cnt += 1
            if cnt >= h:
                l.append(h)
                break
        h += 1
    if len(l)>0:
        return max(l)
    else:
        return 0