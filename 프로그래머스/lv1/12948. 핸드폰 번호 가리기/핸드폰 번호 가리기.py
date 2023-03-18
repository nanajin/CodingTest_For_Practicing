def solution(phone_number):
    answer = ''
    answer += phone_number[:-5:-1] + '*'*(len(phone_number)-4)
    
    return answer[::-1]