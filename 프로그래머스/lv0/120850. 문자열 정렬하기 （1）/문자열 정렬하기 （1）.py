def solution(my_string):
    answer = []
    list = sorted(my_string)
    for i in list:
        if i.isdigit():
            answer.append(int(i))
        else:
            break
    return answer