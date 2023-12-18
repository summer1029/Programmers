def solution(rsp):
    win = ""
    if (len(rsp) > 0 and len(rsp) <= 100) :
        for i in range(len(rsp)) :
            if rsp[i] == "2" :
                win = win + "0"
            if rsp[i] == "0" :
                win = win + "5"
            if rsp[i] == "5" :
                win = win + "2"
    return win