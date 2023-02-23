def solution(order):
    cnt = 0
    list = [3,6,9]
    order = str(order)
    for i in order:
        if int(i) in list:
            cnt += 1
    return cnt