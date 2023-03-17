def solution(today, terms, privacies):
    answer = []
    expired_list = []
    term_dict = {}
    for i in terms:
        i_list = i.split(' ')
        term_dict[i_list[0]] = int(i_list[1])

    for i in privacies:
        i_list = i.split(' ')

        m = term_dict[i_list[1]]
        j_year, j_month, j_day = map(int, i_list[0].split('.'))
        
        e_year = j_year
        e_month = j_month + m
        e_day = j_day - 1
        expired = ''
        
        while e_month > 12:
            e_year += e_month // 12
            e_month = e_month % 12
            if e_month == 0:
                e_year -= 1 
                e_month = 12
        
            if e_day == 0:
                e_day = 28
                e_month -= 1
                if e_month < 0:
                    e_year -= 1
                    e_month = 12


        expired = str(e_year)+'.'+str(e_month).zfill(2)+'.'+str(e_day).zfill(2)
        expired_list.append(expired)

    for i in range(len(expired_list)):
        e_date = expired_list[i].replace('.', '')
        today = today.replace('.', '')
        if int(e_date) < int(today):
            answer.append(i+1)        
    return answer