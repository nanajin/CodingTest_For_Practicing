def solution(n, lost, reserve):
    lost = sorted(lost)
    c_lost = lost[:]
    c_reserve = reserve[:]
    for i in reserve:
        if i in lost:
            c_lost.remove(i)
            c_reserve.remove(i)
    lost = c_lost
    reserve = c_reserve
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            continue
        else:
            n -= 1  
    return n