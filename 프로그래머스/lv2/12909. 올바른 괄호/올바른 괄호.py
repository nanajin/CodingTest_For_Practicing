def solution(s):
    couple = [s[0]]
    for i in s[1:]:
        if len(couple) > 0:
            p = couple.pop()
            if i == ")" and p == "(":
                continue
            else:
                couple.append(p)
                couple.append(i)
        else:
            couple.append(i) 
    if len(couple) > 0:
        return False
    else: return True