def solution(A, B):
    answer = 0
    if len(A) > 0 and len(A) < 100 and len(B) > 0 and len(B) < 100 :
        if A == B :
            answer = 0
        else :
            for i in range(len(A)) :
                A = A[-1] + A[0:len(A) - 1]
                answer = answer + 1
                if A == B :
                    break
            if A != B :
                return -1

    return answer