def solution(n, arr1, arr2):
    answer = ["#"*n]*n
    list1 = [bin(i)[2:].zfill(n) for i in arr1]
    list2 = [bin(i)[2:].zfill(n) for i in arr2]
    change = [] 
    for i in range(n):
        for j in range(n):
            if list1[i][j] == list2[i][j] == '0':
                change.append([i,j])
    for i, j in change:
        l = list(answer[i])
        l[j] = " "
        answer[i] = "".join(l)
    return answer