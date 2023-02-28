def solution(dots):
    dots.sort()
    a = dots[2][1] - dots[3][1]
    b = dots[2][0] - dots[1][0]
    return abs(a*b)