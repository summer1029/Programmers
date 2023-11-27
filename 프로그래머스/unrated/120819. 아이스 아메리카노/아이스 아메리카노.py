def solution(money):
    if(money > 0 and money <= 1000000) :
        coffee = money // 5500
        change = money % 5500
    answer = [coffee, change]
    return answer