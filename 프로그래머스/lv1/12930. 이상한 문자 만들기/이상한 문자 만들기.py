def solution(s):
    answer = ''
    arr = s.split(' ')
    for i in arr:
        for j in range(len(i)):
            if j%2!=0:
                answer += i[j].lower()
            else:
                answer += i[j].upper()
        answer += " "
    return answer[:len(answer)-1]