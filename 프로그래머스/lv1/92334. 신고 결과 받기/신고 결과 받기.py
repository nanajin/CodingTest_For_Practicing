def solution(id_list, report, k):
    answer = []
    report_cnt = {} # 유저별 신고받은 횟수
    report_id = [] # 정지될 유저
    mail_cnt = {} # 메일받을 횟수
    
    report = list(set(report))
    for i in report:
        r_id = i.split(' ')[1]
        if r_id in report_cnt:
            report_cnt[r_id] += 1
        else:
            report_cnt[r_id] = 1
            
    for key, value in report_cnt.items():
        if value >= k:
            report_id.append(key)

    for i in report:
        user = i.split(' ')[0]
        r_id = i.split(' ')[1]
        if r_id in report_id:
            if user in mail_cnt:
                mail_cnt[user] += 1
            else:
                mail_cnt[user] = 1

    for i in id_list:
        if i in mail_cnt:
            answer.append(mail_cnt[i])
        else: answer.append(0)
    return answer