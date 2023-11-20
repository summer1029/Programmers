def solution(str1, str2):
    if (len(str1) >= 1 and len(str1) <= 100 and len(str2) >= 1 and len(str2) <= 100) :
        if (str1.find(str2) >= 0) : # 문자열을 찾고 해당 문자열의 인덱스를 반환해주므로 0보다 크다는 (인덱스는 0부터 시작) 조건을 추가한다
            answer = 1
        else :
            answer = 2
    return answer