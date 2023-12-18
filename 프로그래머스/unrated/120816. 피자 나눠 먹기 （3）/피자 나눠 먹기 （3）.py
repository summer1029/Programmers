def solution(slice, n):
    cnt = 1
    if (slice >= 2 and slice <= 10 and n >= 1 and n <= 100) :
        while n >= slice * cnt :
            cnt = cnt + 1
        if (n == slice * (cnt - 1)) :
            cnt = cnt - 1 
        return cnt