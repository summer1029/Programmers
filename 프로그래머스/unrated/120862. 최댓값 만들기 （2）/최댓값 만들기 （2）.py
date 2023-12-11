def solution(numbers):
    if (len(numbers) >= 2 and len(numbers) <= 100) :
        numbers = sorted(numbers)
        if (numbers[0] * numbers[1] > numbers[-1] * numbers[-2]) :
            max = numbers[0] * numbers[1]
        else :
            max = numbers[-1] * numbers[-2]
    return max