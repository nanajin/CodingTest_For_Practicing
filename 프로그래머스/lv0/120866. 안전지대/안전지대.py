def solution(board):
    answer = 0
    bomb = []
    danger = []
    cnt1 = 0
    n = len(board)
    
    for i in board:
        cnt2 = 0
        for j in i:
            if j == 1:
                bomb.append([cnt1, cnt2])
            cnt2 += 1
        cnt1 += 1
    
    for i in bomb:
        danger.append((i[0]-1, i[1]))
        danger.append((i[0]+1, i[1]))
        danger.append((i[0], i[1]-1))
        danger.append((i[0], i[1]+1))
        danger.append((i[0]-1, i[1]-1))
        danger.append((i[0]-1, i[1]+1))
        danger.append((i[0]+1, i[1]-1))
        danger.append((i[0]+1, i[1]+1))
        danger.append((i[0],i[1]))
    danger = set(danger)
    answer = len(danger)
    for i, j in danger:
        if i < 0 or i > n-1 or j < 0 or j > n-1:
            answer -= 1
    return n**2 - answer