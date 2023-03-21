def solution(s, n):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i == " ":
            answer += " "
        else:
            if i.islower():
                alpha = alpha.lower()
            else:
                alpha = alpha.upper()
            after_idx = alpha.find(i) + n
            if after_idx > 25:
                after_idx -= 26
            answer += alpha[after_idx]
    return answer