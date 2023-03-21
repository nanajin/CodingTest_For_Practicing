def solution(food):
    s = ''
    for i in range(len(food)):
        s += str(i)*(food[i] // 2)
    return s+'0'+s[::-1]
