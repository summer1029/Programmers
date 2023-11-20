def solution(my_string):
    if(len(my_string) >= 1 and len(my_string) <= 100) :
        num = []
        for i in range(len(my_string)) :
            if my_string[i].isdigit() :
                num.append(int(my_string[i])) # 리스트 합치기 : .append(), .insert()       
                answer = sorted(num)
    return answer