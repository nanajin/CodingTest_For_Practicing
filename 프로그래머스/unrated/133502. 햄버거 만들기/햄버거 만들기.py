def solution(ingredient):
    answer= 0
    l = []
    for i in ingredient:
        l.append(i)
        if l[-4:] == [1,2,3,1]:
            for j in range(4):
                l.pop()
            answer += 1
    return answer