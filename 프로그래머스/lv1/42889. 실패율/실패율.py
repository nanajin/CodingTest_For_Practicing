def solution(N, stages):
    fail_percent = []
    for i in range(1,N+1):
        fail_percent.append([0, i])
    clear = len(stages)
    s = list(set(stages))
    for i in s:
        cnt = stages.count(i)
        if i > N:
            continue
        fail_percent[i-1] = [cnt / clear, i]
        # fail_percent.append([cnt / clear, i])
        clear -= cnt

    fail_percent.sort(key=lambda x: (-x[0], x[1]))
    return [i[1] for i in fail_percent]