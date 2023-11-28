def solution(my_string, n):
    result = ''
    if (len(my_string) >= 2 and len(my_string) <= 5 and n >= 2 and n <= 10) :
        for char in my_string :
            result = result + char * n
    return result