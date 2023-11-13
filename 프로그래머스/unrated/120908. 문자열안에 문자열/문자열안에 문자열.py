def solution(str1, str2):
    if len(str1) >= 1 and len(str1) <= 1000 and len(str2) >= 1 and len(str2) <= 1000 :
        # .find는 존재하면 존재하는 문자열의 위치를 반환, 없으면 -1을 반환
        if str1.find(str2) == -1 :
            answer = 2
            return answer
        else : 
            answer = 1
            return answer