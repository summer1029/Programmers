def solution(sides):
    if(len(sides) == 3) :
        sortedSides = sorted(sides)
        if sortedSides[2] < sortedSides[0] + sortedSides[1] :
            return 1
        else :
            return 2
