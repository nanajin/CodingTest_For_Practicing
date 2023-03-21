def solution(numbers, hand):
    answer = ''
    left, right = 10, 12 
    d1, d2 = 0,0
    dic = {1:'L',3:'R', 4:'L', 6:'R', 7:'L', 9:'R'}
    center_dic = {2: [[2],[1,3,5],[4,6,8],[7,9,0],[10,12]],
                 5: [[5],[2,4,6,8],[1,3,7,9,0],[10,12],[]],
                 8: [[8],[5,7,9,0],[2,4,6,10,12],[1,3],[]],
                 0: [[0],[8,10,12],[5,7,9],[2,4,6],[1,3]]}
    for i in numbers:
        if i not in [2,5,8,0]:
            if dic[i] == "L": left = i
            else: right = i 
            answer += dic[i]
        else:
            l = center_dic[i]
            for num in l:
                if left in num:
                    d1 = l.index(num)
                if right in num:
                    d2 = l.index(num)
            if d1 == d2: 
                if hand == "right": 
                    answer += 'R'
                    right = i
                else: 
                    answer += 'L'
                    left = i
            elif d1 < d2: 
                answer += 'L'
                left = i
            else: 
                answer += 'R'  
                right = i
    return answer