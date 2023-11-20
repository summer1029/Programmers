def solution(my_string):
    if len(my_string) >= 5 and len(my_string) <= 100 :
        
        # 방법 1
        # op = []
        # for i in range(len(my_string)) :
        #     if my_string[i] == '+' or my_string[i] == '-' :
        #         op.append(i)
        # sum = int(my_string[0 : op[0]])
        # for i in range(len(op) - 1) :
        #     if my_string[op[i]] == "+" :
        #         sum = sum + int(my_string[op[i] + 1 : op[i + 1]])
        #     elif my_string[op[i]] == "-" :
        #         sum = sum - int(my_string[op[i] + 1 : op[i + 1]])
        # if my_string[op[len(op)-1]] == "+" :
        #     sum = sum + int(my_string[op[-1] + 1 : len(my_string)])
        # elif my_string[op[len(op)-1]] == "-" :
        #     sum = sum - int(my_string[op[-1] + 1 : len(my_string)])
        
        # 방법2
        my_string = my_string.replace(" - ", " + -")
        my_string = my_string.split(" + ")
        sum = 0
        for i in my_string:
            sum = sum + int(i)
        
    return sum