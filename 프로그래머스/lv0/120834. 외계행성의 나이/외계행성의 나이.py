def solution(age):
    answer = ''
    num = 0
    dict = {}
    alpha = 'abcdefghij'
    for i in alpha:
        dict[num] = i
        num += 1

    for j in str(age):
        answer += dict[int(j)]
    return answer