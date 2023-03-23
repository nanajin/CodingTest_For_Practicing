def solution(keymap, targets):
    answer = []
    key_dic = {}
    for i in keymap:
        for j in range(len(i)):
            if i[j] in key_dic:
                key_dic[i[j]].append(j+1)
            else:
                key_dic[i[j]] = [j+1]
    for i in targets:
        cnt = 0
        for j in i:
            if j not in key_dic:
                cnt = -1
                break
            else:
                cnt += min(key_dic[j])
        answer.append(cnt)
    return answer