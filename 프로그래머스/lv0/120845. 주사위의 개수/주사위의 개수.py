def solution(box, n):
    ans = 1
    for i in box:
        ans *= i // n
    return ans