# def is_prime(num):
#     p_list = []
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#         	is_prime(num % i)
#         else:
#             p_list.append(num % i)
#     return p_list

def solution(n):
    answer = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
            if i not in answer:
                answer.append(i)
        else:
            i += 1
        
    return answer