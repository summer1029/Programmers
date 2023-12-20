def solution(n):
    if (n >= 1 and n <= 10000) :
        divisor = []
        for i in range(1, n + 1) :
            if n % i == 0 :
                divisor.append(i)
    return divisor