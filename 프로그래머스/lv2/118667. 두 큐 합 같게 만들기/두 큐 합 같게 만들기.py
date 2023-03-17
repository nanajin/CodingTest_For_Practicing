from collections import deque
def solution(q1, q2):
    cnt = 0
    s1, s2 = sum(q1), sum(q2)
    equal = (s1+s2) // 2
    l = len(q1)
    q1, q2 = deque(q1), deque(q2)
    while 1:
        if s1 == s2:
            return cnt
        if s1 > equal:
            move = q1[0]
            s2 += move
            s1 -= move
            q2.append(move)
            q1.popleft()
            # q1.pop(0)

        else:
            move = q2[0]
            s1 += move
            s2 -= move
            q1.append(move)
            q2.popleft()
            # q2.pop(0)

        cnt += 1
        
        if cnt > l*4:
            return -1