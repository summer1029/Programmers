def solution(num, k):
    if (num > 0 and num < 1000000) :
        string = str(num)
        for i in range(len(string)) :
            if string[i] == str(k):
                return i + 1
        return -1