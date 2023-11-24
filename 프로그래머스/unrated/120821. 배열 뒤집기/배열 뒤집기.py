def solution(num_list):
    answer = []
    if (len(num_list) >= 1 and len(num_list) <= 1000) :
        for i in range(len(num_list) - 1, -1, -1) :
            if(num_list[i] >= 0 and num_list[i] <= 1000) :
                answer.append(num_list[i])
    return answer