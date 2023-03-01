def solution(quiz):
    answer = []
    for i in quiz:
        sik = i.replace(" ", "").split("=")
        res = eval(sik[0])
        if res == int(sik[1]):
            answer.append("O")
        else: answer.append("X")
    return answer