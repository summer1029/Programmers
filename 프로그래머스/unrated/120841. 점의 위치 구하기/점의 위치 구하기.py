def solution(dot):
    if (len(dot) == 2) :
        if (dot[0] > 0 and dot[1] > 0) :
            return 1
        elif (dot[0] < 0 and dot[1] > 0) :
            return 2
        elif (dot[0] < 0 and dot[1] < 0) :
            return 3
        elif (dot[0] > 0 and dot[1] < 0) :
            return 4