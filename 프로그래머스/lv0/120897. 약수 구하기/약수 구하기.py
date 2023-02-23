def solution(n):
    list = []
    list_back = [] 

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            list.append(i)
            if (i != (n // i)): 
                list_back.append(n//i)

    return list + list_back[::-1]