def solution(arr1, arr2):
    answer = []
    for n in arr1:
        l = []
        j = 0
        while j < len(arr2[0]):
            sero = []
            gop = 0
            for i in arr2:
                sero.append(i[j])
            for i in range(len(sero)):
                gop += n[i] * sero[i]
            l.append(gop)
            j += 1
        answer.append(l)
    return answer