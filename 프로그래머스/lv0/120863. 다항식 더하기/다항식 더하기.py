def solution(polynomial):
    answer = ''
    x_answer, su_answer = '', ''
    x_hang, su_hang = 0, 0
    polynomial = polynomial.replace(' ', '')
    p_list = polynomial.split("+")
    for i in p_list:
        if i == 'x':
            p_list[p_list.index(i)] = '1x'
    for i in p_list:
        if 'x' in i:
            x_hang += int(i.replace('x', ''))
        else:
            su_hang += int(i)
    if x_hang != 0:
        if str(x_hang) == '1':
            x_answer += 'x'
        else: x_answer += str(x_hang)+'x'
    else:
        answer += str(su_hang)
    if su_hang != 0:
        su_answer += str(su_hang)
    else:
        answer += str(x_answer)
    if x_hang != 0 and su_hang != 0:
        answer = x_answer+' + '+su_answer
    elif x_hang == 0 and su_hang == 0:
        return 0
    return answer