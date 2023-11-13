def solution(str1, str2):
    if len(str1) >= 1 and len(str1) <= 1000 and len(str2) >= 1 and len(str2) <= 1000 :
        if str1.find(str2) >= 0 :
            answer = 1
            return answer
        else : 
            answer = 2
            return answer