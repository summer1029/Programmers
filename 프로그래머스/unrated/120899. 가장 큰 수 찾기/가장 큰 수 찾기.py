def solution(array):
    if (len(array) >= 1 and len(array) <= 100) :
        max = array[0]
        for i in range(1, len(array)) :
            if max < array[i] :
                max = array[i]
        result = [max, array.index(max)]
    return result