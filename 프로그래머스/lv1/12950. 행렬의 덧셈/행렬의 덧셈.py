def solution(arr1, arr2):
    answer = [[0]*len(arr1[0])]*len(arr1)
    for i in range(len(arr1)):
        a = [0]*len(arr1[0])
        for j in range(len(arr1[0])):
            a[j] = arr1[i][j] + arr2[i][j]
        answer[i] = a
    return answer