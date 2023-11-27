def solution(numbers, direction):
    answer = [] 
    if (len(numbers) >= 3 and len(numbers) <= 20) :
        if (direction == "left") :
            return numbers[1:len(numbers)] + [numbers[0]]
            
        else :
            return [numbers[-1]] + numbers[0:-1]
    
    return answer