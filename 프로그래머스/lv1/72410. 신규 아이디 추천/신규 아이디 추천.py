def solution(new_id):
    ch = ["~!@#$%^&*()=+[{]}:?,<>/"]
    dots = ["." * x for x in range(15,1,-1)]
    #1
    new_id = new_id.lower()
    #2
    for i in new_id:
        if i in ch[0]:
            new_id = new_id.replace(i, "")
    #3
    for i in dots:
        if i in new_id:
            new_id = new_id.replace(i, ".")
    id = list(new_id)
    #4
    if id[0] == ".":
        id.pop(0)
    elif id[-1] == ".":
        id.pop(-1)
    #5
    if len(id) == 0:
        id.append("a")
    #6
    elif len(id) > 15:
        id = id[:15]
    if id[-1] == ".":
        id.pop(-1)
    #7
    while len(id) < 3:
        id.append(id[-1])
    return "".join(id)