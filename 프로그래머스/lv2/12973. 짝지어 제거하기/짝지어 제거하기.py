def solution(s):
    s = list(s)
    remain = [s[0]]
    i = 1
    while i < len(s):
        if len(remain) > 0:
            p = remain.pop()
            if p == s[i]:
                i += 1
                continue
            else:
                remain.append(p)
                remain.append(s[i])
        else:
            remain.append(s[i])
        i += 1
    if len(remain) == 0:
        return 1
    return 0