def yaksu(x):
    cnt = 0
    y_list = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            if i not in y_list:
                y_list.append(i)
            if (x // i) not in y_list:
                y_list.append(x // i)
    return len(y_list)
            
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = yaksu(i)
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer