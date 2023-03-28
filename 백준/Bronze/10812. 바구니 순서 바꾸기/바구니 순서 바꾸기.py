n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    pick = basket[i-1:j]
    rotate=[]
    mid = basket[k-1]
    idx = pick.index(mid)
    for a in range(j-i+1):
        if idx+a >= len(pick):
            rotate.append(pick[(idx + a)-len(pick)])
        else:
            rotate.append(pick[idx + a])
    basket[i-1:j] = rotate
for b in basket:
    print(b, end=" ")