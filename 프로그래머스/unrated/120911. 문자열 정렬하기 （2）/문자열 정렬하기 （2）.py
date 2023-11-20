def solution(my_string):
    answer = ''
    if(len(my_string) > 0 and len(my_string) < 100) :
        my_string = my_string.lower()
        sort = sorted(my_string)
        for i in sort :
            answer = answer + i
    return answer