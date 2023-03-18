def prime(x):
    if x == 1:
        return False
    for i in range (2, int(x**0.5 + 1)):	
    	if x % i == 0:
        	return False
    return True
def solution(n, k):
    answer = 0
    value = ''
    while n > 0:
        value += str(n % k)
        n //= k

    value = value[::-1].split('0')
    for i in value:
        if i != '':
            if prime(int(i)):
                answer += 1
    return answer