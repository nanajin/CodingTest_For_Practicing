import numpy as np
def solution(n):
    answer = 0
    if n % np.sqrt(n) == 0:
        return 1
    else:
        return 2