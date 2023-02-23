def solution(array):
    answer = []
    new_arr = sorted(array)
    answer.append(new_arr[-1])
    answer.append(array.index(new_arr[-1]))
    return answer