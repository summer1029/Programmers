def solution(num_list, n):
    i = 0
    answer = []
    while i < len(num_list) :
        answer.append(num_list[i : i + n])
        i = i + n
    return answer