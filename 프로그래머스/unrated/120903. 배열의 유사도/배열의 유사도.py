def solution(s1, s2):
    same = 0
    if(len(s1) >= 1 and len(s1) <= 100 and len(s2) >= 1 and len(s2) <= 100) :
        for i in range(len(s1)) :
            for j in range(len(s2)) :
                if (len(s1[i]) >= 1 and len(s1[i]) <= 10 and len(s2[j]) >= 1 and len(s2[j]) <= 10 and s1[i] == s2[j]) :
                    same = same + 1 
    return same