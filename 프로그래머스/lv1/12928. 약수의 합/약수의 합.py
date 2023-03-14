def solution(n):
    yaksu = []
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    else:
        answer = 0
        yaksu.append(1)
        yaksu.append(n)
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                if n//i not in yaksu:
                    yaksu.append(n//i)
                if i not in yaksu:
                    yaksu.append(i)

    answer += sum(yaksu)
    return answer