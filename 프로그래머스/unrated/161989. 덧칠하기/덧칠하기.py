def solution(n, m, section):
    l = []
    cnt  = 1
    init = 0
    painted = []
    while 1:
        if len(painted) == len(section):
            break
        last = section[init] + m - 1
        for i in range(init, len(section)):
            if section[i] <= last:
                painted.append(section[i])
                continue
            cnt += 1
            init = i
            break
    # while 1:
    #     if len(section) == 0:
    #         break
    #     for i in section:   
    #         if i in range(section[0],section[0]+m):
    #             copy.remove(i)
    #     section = copy
    #     cnt += 1
    return cnt