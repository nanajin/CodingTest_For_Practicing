def solution(array):
    answer = 0
    string = ''
    for i in array:
        string += str(i)
    
    return string.count('7')