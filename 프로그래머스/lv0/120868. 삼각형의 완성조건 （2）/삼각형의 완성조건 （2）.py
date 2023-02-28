def solution(sides):
    sides.sort()
    s = sum(sides)
    m = sides[1]
    answer = s -m
    b = sides[1]-sides[0] +1
    for i in range(b, m):
        answer += 1
    return answer