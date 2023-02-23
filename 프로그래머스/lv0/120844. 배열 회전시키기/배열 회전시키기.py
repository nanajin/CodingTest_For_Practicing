def solution(numbers, direction):
    if direction == 'right':
        x = numbers[-1]
        numbers.remove(x)
        numbers.insert(0, x)
    else:
        x = numbers[0]
        numbers.remove(x)
        numbers.append(x)
        
    return numbers