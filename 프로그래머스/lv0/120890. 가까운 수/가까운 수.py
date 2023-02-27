def solution(array, n):
    list = []
    array.append(n)
    array.sort()
    idx = array.index(n)
    if idx == len(array)-1:
        return array[idx-1]
    else:
        prev_v = array[idx]-array[idx-1]
        next_v = array[idx+1]-array[idx]
    
        if prev_v > next_v:
            return array[idx+1]
        elif prev_v < next_v:
            return array[idx-1]
        else:
            return array[idx-1]
