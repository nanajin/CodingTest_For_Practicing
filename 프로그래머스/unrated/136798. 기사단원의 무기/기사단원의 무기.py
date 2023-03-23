def yaksu(x):
    cnt = 0
    l = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            if i not in l:
                l.append(i)
            if (x // i) not in l:
                l.append(x // i)
    return len(l)
def solution(number, limit, power):
    answer = 0
    yaksu_list = [1]
    for i in range(2, number+1):
        yaksu_list.append(yaksu(i))
    for i in range(len(yaksu_list)):
        if yaksu_list[i] > limit:
            yaksu_list[i] = power
    
    return sum(yaksu_list)