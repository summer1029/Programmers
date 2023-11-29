def solution(my_string):
    sum = 0
    
    if(len(my_string) >= 1 and len(my_string) <= 1000) :
        for num in my_string :
            if num.isdigit() == True :
                sum = sum + int(num)
    return sum