def solution(quiz):
    answer = []
    for expression in quiz :
        ex = expression.split(" ")
        if ex[1] == "+" :
            if int(ex[0]) + int(ex[2]) == int(ex[4]) :
                answer.append("O")
            else :
                answer.append("X")
        if ex[1] == "-" :
            if int(ex[0]) - int(ex[2]) == int(ex[4]) :
                answer.append("O")
            else :
                answer.append("X")
    return answer