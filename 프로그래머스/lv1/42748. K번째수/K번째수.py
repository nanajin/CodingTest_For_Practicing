def solution(array, commands):
    answer = []
    for i in commands:
        i, j, k = i[0], i[1], i[2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer