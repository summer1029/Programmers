def solution(n):
    # 소인수 분해 코드
    prime_num = []
    prime = []
    num = 2
    while num <= n :
        if n % num == 0 :
            prime_num.append(num)
            n = n // num
        elif n % num != 0 :
            num = num + 1
    for i in prime_num :
        if i not in prime :
            prime.append(i)
    return prime
    