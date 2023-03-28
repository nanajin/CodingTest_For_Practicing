n, m = map(int, input().split())
basket = {}
for i in range(1,n+1):
    basket[i] = i
for _ in range(m):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]
for i in basket.values():
    print(i, end=" ")