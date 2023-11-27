import math

def solution(array):
    if(len(array) % 2 != 0 and len(array) > 0 and len(array) < 100) :
        for i in range(len(array)) :
            if(array[i] > -1000 and array[i] < 1000) :
                array.sort()
    return array[math.floor(len(array) / 2 )]