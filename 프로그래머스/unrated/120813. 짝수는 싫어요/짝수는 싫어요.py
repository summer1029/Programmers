def solution(n):
    odd = []
    if (n >= 1 and n <= 100) :
        for i in range(n+1) :
            if i % 2 != 0 :
                odd.append(i)
    return sorted(odd)