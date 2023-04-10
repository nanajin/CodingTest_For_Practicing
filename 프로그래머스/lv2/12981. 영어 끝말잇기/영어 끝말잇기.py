def solution(n, words):
    l = [words[0]]
    cnt = 1
    fail = False
    for i in words[1:]:
        cnt += 1
        if l[-1][-1] != i[0]:
            fail = True
            break
        if i in l:
            fail = True
            break
        l.append(i)
    if cnt == len(words) and fail == False:
        return [0,0]
    else:
        div, mod = divmod(cnt, n)
    if mod == 0: 
        return [n, div]
    return [mod, div+1]