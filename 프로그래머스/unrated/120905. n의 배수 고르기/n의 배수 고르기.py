def solution(n, numlist):
    result = []
    if(n >= 1 and n <= 10000 and len(numlist) >= 1 and len(numlist) <= 100) :
        for i in range(len(numlist)) :
            if(numlist[i] % n == 0) :
                result.append(numlist[i])
    return result