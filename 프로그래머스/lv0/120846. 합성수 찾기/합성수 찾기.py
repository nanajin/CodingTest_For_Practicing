import math

def prime(x):
    for i in range (2, int(x**0.5 + 1)):	
    	if x % i == 0:
        	return False
    return True
                    
def solution(n):
    for i in range(1, n+1):
        if prime(i):
            n -= 1
    return n