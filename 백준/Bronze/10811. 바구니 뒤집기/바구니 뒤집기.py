n, m = map(int, input().split())
basket = [i for i in range(1,n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    a = basket[i-1:j]
    a.reverse()
    basket[i-1:j] = a
for i in basket:
    print(i, end=" ")