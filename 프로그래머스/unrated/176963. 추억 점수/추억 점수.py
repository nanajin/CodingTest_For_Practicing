def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for i in photo:
        memory = 0
        for j in i:
            if j in dic:
                memory += dic[j]
        answer.append(memory)
    return answer