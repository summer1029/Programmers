def solution(before, after):
    if (len(before) >= 0 and len(before) <= 1000 and len(after) >= 0 and len(after) <= 1000) :
        if (sorted(before) == sorted(after)) :
            return 1
        else :
            return 0
