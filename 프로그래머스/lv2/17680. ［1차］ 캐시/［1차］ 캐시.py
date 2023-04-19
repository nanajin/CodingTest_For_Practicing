from collections import deque
def solution(cacheSize, cities):
    answer = 0
    hit, miss = 1, 5
    l = deque(maxlen=cacheSize)
    for i in cities:
        i = i.lower()
        if i in l:
            answer += hit
            l.remove(i)
            l.append(i)
        else:
            l.append(i)
            answer += miss
    return answer