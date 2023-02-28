def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw == i:
            answer = 'login'
            break
        elif id_pw[0] in i:
            answer = 'wrong pw'
            break
        else:
            answer = 'fail'
                
    return answer