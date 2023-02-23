def solution(my_string, num1, num2):
    l = list(my_string)
    str = ''
    l[num1], l[num2] = l[num2], l[num1]

    for i in l:
        str += i
    return str


   