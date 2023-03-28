def solution(s):
    remove_zero = 0
    cnt = 0
    while s != "1":
        remove_zero += s.count("0")
        s = s.replace("0","")
        c = len(s)
        s = bin(c)[2:]
        cnt += 1
    return [cnt, remove_zero]