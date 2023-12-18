def solution(slice, n):
    # 방법1
    # cnt = 1
    # if (slice >= 2 and slice <= 10 and n >= 1 and n <= 100) :
    #     while n >= slice * cnt :
    #         cnt = cnt + 1
    #     if (n == slice * (cnt - 1)) :
    #         cnt = cnt - 1 
    #     return cnt
    
    # 방법2
    if (slice >= 2 and slice <= 10 and n >= 1 and n <= 100) :
        if (n % slice > 0) :
            cnt = n // slice + 1
        else :
            cnt = n // slice
        return cnt
    