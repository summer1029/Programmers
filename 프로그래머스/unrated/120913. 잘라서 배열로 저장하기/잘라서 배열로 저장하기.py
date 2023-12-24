def solution(my_str, n):
    if len(my_str) >= 1 and len(my_str) <= 100 :
        result = []
        for idx in range(0, len(my_str), n) :
            result.append(my_str[idx : idx + n])
    return result