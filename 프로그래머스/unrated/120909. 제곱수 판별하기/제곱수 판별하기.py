import math

def solution(n):
    if (n >= 1 and n <= 1000000) :
        result = math.sqrt(n)
        if(result.is_integer()) :
            return 1
        else :
            return 2