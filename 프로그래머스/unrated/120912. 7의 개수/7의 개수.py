def solution(array):
    count = 0
    for s in range(len(array)) :
        s = str(array[s])
        for idx in range(len(s)) :
            if s[idx] == str(7) :
                count = count + 1
    return count