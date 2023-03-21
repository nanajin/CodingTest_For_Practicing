def solution(a, b):
    # date = {1:'MON',2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT',7:'SUN'}
    date = {0: 'THU',1:'FRI',2:'SAT',3:'SUN',4:'MON',5:'TUE',6:'WED'}
    day = b
    if a == 1:
        return date[day % 7]
    for i in range(1,a):
        if i in [1,3,5,7,8,10,12]:
            day += 31
        elif i == 2:
            day += 29
        else: 
            day += 30
    return date[day % 7]