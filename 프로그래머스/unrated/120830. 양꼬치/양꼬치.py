def solution(n, k):
    price = 0
    if n > 0 and n < 1000 and k >= n // 10 and k < 1000 :
        price = n * 12000 + k * 2000
        if n >= 10 :
            price = price - 2000 * (n // 10)
    
    return price