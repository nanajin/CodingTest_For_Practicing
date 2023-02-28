def solution(keyinput, board):
    answer = []
    x_restrict = board[0]//2
    y_restrict = board[1]//2
    dic = {"left":-1, "right":1, "down":-1, "up":1}
    lr, ud = 0, 0
    for i in keyinput:
        if i == "left" or i == "right":
            lr += dic[i]
            if abs(lr) > x_restrict:
                if lr < 0:
                    lr = -x_restrict
                else:
                    lr = x_restrict
                continue
        else:
            ud += dic[i]
            if abs(ud) > y_restrict:
                if ud < 0:
                    ud = -y_restrict
                else:
                    ud = y_restrict
                continue
    # if abs(lr) > x_restrict:
    #     if lr < 0:
    #         lr = -x_restrict
    #     else:
    #         lr = x_restrict
    # if abs(ud) > y_restrict:
    #     if ud < 0:
    #         ud = -y_restrict
    #     else:
    #         ud = y_restrict
    return [lr,ud]