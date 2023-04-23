def solution(board, moves):
    answer = 0
    basket = []
    l = [list(x) for x in zip(*board)]
    for i in moves:
        d = 0
        while len(l[i-1]) > 0:
            d = l[i-1].pop(0)
            if d == 0:
                continue
            else:
                break
        if d != 0: 
            if len(basket)!=0 and basket[-1] == d:
                answer += 2
                basket.pop()
            else:
                basket.append(d)
    return answer