from collections import deque
def solution(cards1, cards2, goal):
    goal, cards1, cards2 = deque(goal), deque(cards1), deque(cards2)
    while len(goal) > 0:
        word = goal.popleft()
        if len(cards1) > 0 and cards1[0] == word:
            cards1.popleft()
            continue
        elif len(cards2) > 0 and cards2[0] == word:
            cards2.popleft()
            continue
        else:
            return "No"
    return "Yes"