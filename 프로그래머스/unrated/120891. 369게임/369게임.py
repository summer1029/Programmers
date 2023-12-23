def solution(order):
    clap = 0
    if (order >= 1 and order <= 1000000) :
        string_order = str(order)
        for i in range(len(string_order)) :
            if string_order[i] == str(3) or string_order[i] == str(6) or string_order[i] == str(9) :
                clap = clap + 1
    return clap