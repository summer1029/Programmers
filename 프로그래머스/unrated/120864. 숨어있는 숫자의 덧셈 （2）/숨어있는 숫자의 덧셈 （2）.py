def solution(my_string):
    for alpha in my_string :
        if alpha.isalpha() == True :
            my_string = my_string.replace(alpha, " ")
    num = my_string.split(" ")
    sum = 0
    for number in num :
        if number.isnumeric() == True :
            sum = sum + int(number)
    return sum
            