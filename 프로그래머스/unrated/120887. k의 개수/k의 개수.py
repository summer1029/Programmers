def solution(i, j, k):
    count = 0
    for s in range(i, j + 1) :
        s = str(s)
        for idx in range(len(s)) :
            if s[idx] == str(k) :
                count = count + 1
    return count