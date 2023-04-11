def isExist(s):
    possible = ["aya", "ye", "woo", "ma"]
    for i in possible:
        if i in s:
            return s.replace(i,' ')
    return "0"
def solution(babbling):
    answer = 0
    repeat = ["ayaaya", "yeye", "woowoo", "mama"]
    # while 1:
    #     for i in babbling:
    #         if repeat[j] in i:
                
    for i in range(len(babbling)):
        for j in repeat:
            if j in babbling[i]:
                babbling[i] = ""
                break
    for i in babbling:
        s = isExist(i)
        while 1:
            if s == "0":
                break
            if s.replace(" ","") == "":
                answer += 1
                break
            s = isExist(s)

    # for i in babbling:
    #     while 1:
    #         if possible[j] in i:
    #             i = i.replace(possible[j],'')
    #             j = -1
    #         elif j == len(possible)-1:
    #             break
    #         elif i == '':
    #             answer += 1
    #             break
    #         j += 1
    return answer
