def solution(my_string):
    answer = 0
    num = ''
    for i in my_string:
        if i.isdigit():
            num += i
        else:
            if num != '':
                answer += int(num)
                num = ''
            continue

    if num != '':
        answer += int(num)
    
    if answer == 0:
        return 0
    return answer