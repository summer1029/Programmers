def solution(n):
    count = 0
    if(n >= 1 and n <= 1000000) :
        for i in range(1, n+1) :
            if (n % i == 0) :
                count = count + 1
    return count