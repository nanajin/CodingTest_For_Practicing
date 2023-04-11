def yaksu(num):
    y = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            y.append([num // i, i])
    return y
        
def solution(brown, yellow):
    y = yaksu(brown + yellow)
    i = -1
    while 1:
        if (y[i][0]-2) * (y[i][1]-2) == yellow:
            return y[i]
        i -= 1
        