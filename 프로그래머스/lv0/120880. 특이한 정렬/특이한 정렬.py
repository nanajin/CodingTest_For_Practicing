def solution(numlist, n):
    new_list = []
    for i in numlist:
        new_list.append([abs(n-i),i])
    new_list.sort(key=lambda x: (x[0], -x[1]))
    return [i[1] for i in new_list]