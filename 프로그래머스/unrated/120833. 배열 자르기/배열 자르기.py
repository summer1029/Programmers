def solution(numbers, num1, num2):
    
    if(len(numbers) >= 2 and len(numbers) <= 30) :
        for i in range(len(numbers)) :
            if (numbers[i] >= 0 and numbers[i] <= 1000) :
                    return numbers[num1:num2 + 1]