def solution(num_list):
    even = 0
    odd = 0
    
    if (len(num_list) >= 1 and len(num_list) <= 100) :
        for i in range(len(num_list)) :
            if (num_list[i] >= 0 and num_list[i] <= 1000) :
                if (num_list[i] % 2 == 0) :
                    even = even + 1
                else :
                    odd = odd + 1
    return [even, odd]