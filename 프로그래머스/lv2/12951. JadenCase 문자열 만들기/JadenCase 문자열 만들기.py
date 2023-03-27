def solution(s):
    s = s.split(" ")
    a = ''
    for i in range(len(s)):
        if s[i] != "":
            a = s[i][0].upper()
            a += s[i][1:].lower()
            s[i] = a
    return ' '.join(s)