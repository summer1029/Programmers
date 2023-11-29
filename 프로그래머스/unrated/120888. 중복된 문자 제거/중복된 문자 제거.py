def solution(my_string):
    result = ''
    if(len(my_string) >= 1 and len(my_string) <= 110) :
        for char in my_string :
            if char not in result :
                result = result + char
    return result