def solution(n):
    count = 0
    
    if n >= 1 and n <= 100 :
        for num in range(1, n + 1) :
            division = 0
            for i in range(1, num + 1) :
                if num % i == 0 :
                    division = division + 1
            if division >= 3 :
                count = count + 1
    return count