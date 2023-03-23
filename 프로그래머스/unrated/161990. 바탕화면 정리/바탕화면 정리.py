def solution(wallpaper):
    loc_list = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                loc_list.append([i, j])
    lux = loc_list[0][0]
    rdx = loc_list[-1][0] + 1
    loc_list.sort(key=lambda x: x[1])
    luy = loc_list[0][1]
    rdy = loc_list[-1][1] + 1
    return [lux, luy, rdx, rdy]