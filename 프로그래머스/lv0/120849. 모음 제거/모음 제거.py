def solution(my_string):
    moum = 'aeiou'
    for i in my_string:
        if i in moum:
            my_string = my_string.replace(i, '')
    return my_string