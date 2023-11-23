def solution(n, k):
    price = 0
    
    price = n * 12000 + k * 2000
    if n >= 10 :
        price = price - 2000 * (n // 10)
    
    return price