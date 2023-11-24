def solution(n):
    sum = 0
    if (n >= 0 and n <= 1000000) :
        s = str(n)
        for i in range(len(s)) :
            sum = sum + int(s[i])
    return sum