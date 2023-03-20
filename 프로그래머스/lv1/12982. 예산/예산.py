def solution(d, budget):
    d.sort()
    while 1:
        if sum(d) > budget:
            d.pop()
        else:
            return len(d)