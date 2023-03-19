def solution(s):
    cnt = 0
    for i in s:
        if i.isdigit():
            cnt += 1
    if cnt == len(s) and (len(s) == 4 or len(s) == 6):
        return True
    return False