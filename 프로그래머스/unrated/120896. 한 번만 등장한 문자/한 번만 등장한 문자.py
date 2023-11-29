def solution(s):
    # 방법 1
    # answer = []
    # for char in s :
    #     if s.count(char) == 1 :
    #         answer.append(char)
    # return "".join(sorted(answer))
    
    # 방법 2
    sort = sorted(s)
    result = ""
    for i in range(len(sort)) :
        count = 0
        for j in range(len(sort)) :
            if sort[i] == sort[j] :
                count = count + 1
        if count == 1 :
            result = result + sort[i]
    return result