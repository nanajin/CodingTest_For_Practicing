def solution(numbers):
    answer = ''
    word = ''
    alpha = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', 
               "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    num_list = []
    for i in range(0,len(numbers)):
        if word in alpha:
            answer += alpha[word]
            word = ''
        word += numbers[i]
    return int(answer+alpha[word])