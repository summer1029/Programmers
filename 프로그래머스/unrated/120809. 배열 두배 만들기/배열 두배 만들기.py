def solution(numbers):
    double = []
    if (len(numbers) >= 1 and len(numbers) <= 1000) :
        for i in range(len(numbers)) :
            if(numbers[i] >= -10000 and numbers[i] <= 10000) :
                double.append(2*numbers[i])
    return double