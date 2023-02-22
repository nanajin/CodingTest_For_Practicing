def solution(my_string):
    cnt = 0
    num_str = '123456789'
    list = sorted(my_string)

    for i in list:
        if i in num_str:
            cnt += int(i)
        else:
            break
    return cnt
            