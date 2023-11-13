def solution(my_string):
    answer = ''

    # 방법 for-loop 이용
    if len(my_string) >= 1 and len(my_string) <= 1000 :
        for i in range(len(my_string) - 1, -1, -1) :
            answer = answer + my_string[i]
    return answer
    
    # 방법 2 - slicing 이용
    # if len(my_string) >= 1 and len(my_string) <= 1000 :
    #     answer = my_string[::-1]
    # return answer

    # 방법 3 - .join(reversed()) 이용
    # answer = answer.join(reversed(my_string))
    # return answer

