score_sum, all_score = 0, 0
grade_dic = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0,
             "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
score_l = []
for _ in range(20):
    subject, score, grade = map(str, input().split())
    if grade == "P":
        continue
    score_l.append(int(score[0]))
    all_score += grade_dic[grade] * int(score[0])
score_sum = sum(score_l)
print(f'{all_score / score_sum:2f}')