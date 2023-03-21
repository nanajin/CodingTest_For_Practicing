def solution(s):
    answer = []
    str_dict = {}
    for i in range(len(s)):
        if s[i] not in str_dict:
            answer.append(-1)
        else:
            answer.append(i - str_dict[s[i]])
        str_dict[s[i]] = i
    return answer