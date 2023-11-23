def solution(n):
    sum = 0
    if n >= 0 and n <= 1000 :
        for i in range(0, n+1) :
            if i % 2 == 0 :
                sum = sum + i
    return sum