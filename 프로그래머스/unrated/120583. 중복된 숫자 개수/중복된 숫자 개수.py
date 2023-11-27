def solution(array, n):
    count = 0
    if(len(array) >= 1 and len(array) <= 100 and n >= 0 and n <= 1000) :
        for i in range(len(array)) :
            if(array[i] >= 0 and array[i] <= 1000 and array[i] == n) :
                count = count + 1

    return count