def solution(array, height):
    count = 0
    if (len(array) >= 1 and len(array) <= 100 and height >= 1 and height <= 200) :
        for i in range(len(array)) :
            if(array[i] >= 1 and array[i] <= 200) :
                if array[i] > height :
                    count = count + 1
    return count