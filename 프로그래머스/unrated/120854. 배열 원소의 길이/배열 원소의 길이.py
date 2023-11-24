def solution(strlist):
    answer = []
    for i in range(len(strlist)) :
        if (len(strlist[i]) >= 1 and len(strlist[i]) <= 100) :
            answer.append(len(strlist[i]))
    return answer