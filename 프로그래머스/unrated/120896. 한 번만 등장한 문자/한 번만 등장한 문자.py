def solution(s):
    sort = sorted(s)
    result = ''
    
    for i in range(len(sort)) :
        count = 0
        for j in range(len(sort)) :
            if sort[i] == sort[j] :
                count = count + 1
        if count == 1 :
            result = result + sort[i]
    return result