def solution(A, B):
    cnt = 1
    if A == B:
        return 0
    for i in range(len(A)+1):
        A = A[-1]+A[0:len(A)-1]
        if A == B:
            return cnt
        cnt += 1
    return -1