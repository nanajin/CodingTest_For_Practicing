from itertools import *
def solution(numbers):
    answer = []
    l = list(combinations(numbers,2))
    for i in l:
        if sum(i) not in answer:
            answer.append(sum(i))
    return sorted(answer)