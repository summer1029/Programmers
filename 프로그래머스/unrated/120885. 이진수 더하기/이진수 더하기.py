def solution(bin1, bin2):
    # 10진수 n진수 변환 > int()함수 사용
    # 2진수 ➡️ 10진수 : int(num, 2)
    # 8진수 ➡️ 10진수 : int(num, 8)
    # 16진수 ➡️ 10진수 : int(num, 16)
    
    # oct()함수
    # 10진수 ➡️ 8진수 문자열
    
    # hex()함수
    # 10진수 ➡️ 16진수 문자열
    
    # bin()함수
    # 10진수 ➡️ 2진수 문자열
    
    x = int(bin1, 2)
    y = int(bin2, 2)
    sum = x + y
    result = bin(sum).replace("0b", "")
    return result