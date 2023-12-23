import math
def solution(n):
    # 방법 1
    # if n > 0 and n <= 3628800 :
    #     for i in range(11) :
    #         if math.factorial(i) <= n :
    #             result = i
    # return result

    # 방법 2
    # if n > 0 and n <= 3628800 :
    #     factorial = 1
    #     for i in range(1, 11) :
    #         factorial = factorial * i
    #         if factorial <= n :
    #             result = i
    #     return result
    
    # 방법 3
    factorial = 1
    i = 1
    while factorial <= n :
        factorial = factorial * i
        i = i + 1
        if factorial > n :
            i = i - 2
    return i
