def yaksu(x):
    l = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            l.append(i)
            l.append(x // i)
    return len(set(l))
def solution(number, limit, power):
    answer = 0
    yaksu_list = [1]
    for i in range(2, number+1):
        yaksu_list.append(yaksu(i))
    for i in yaksu_list:
        if i > limit:
            answer += power
        else:
            answer += i
    return answer