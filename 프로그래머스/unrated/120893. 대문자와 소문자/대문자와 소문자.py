def solution(my_string):
    # 방법 1
    # if(len(my_string) >= 1 and len(my_string) <= 1000) :
    #     return my_string.swapcase()
    
    # 방법 2
    if(len(my_string) >= 1 and len(my_string) <= 1000) :
        result = ''
        for i in my_string :
            if i.islower() == True :
                result = result + i.upper()
            if i.isupper() == True :
                result = result + i.lower()
        return result
