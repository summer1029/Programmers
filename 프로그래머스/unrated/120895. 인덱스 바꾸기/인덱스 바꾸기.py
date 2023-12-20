def solution(my_string, num1, num2):
    new = ''
    if(len(my_string) > 1 and len(my_string) < 100) :
        my_string = list(my_string) 
        temp = my_string[num1]
        my_string[num1] = my_string[num2]
        my_string[num2] = temp
    return new.join(my_string)