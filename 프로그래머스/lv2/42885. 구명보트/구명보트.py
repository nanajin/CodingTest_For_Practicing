from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    while len(people) > 1:
        if people[0]+people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.popleft()
    answer += len(people)
    # if len(people) % 2 != 0:
    #     people.pop()
    #     answer += 1
    # for i in range(0,len(people),2):
    #     if people[i]+people[i+1] <= limit:
    #         answer += 1
    #     else:
    #         answer += 2
    return answer