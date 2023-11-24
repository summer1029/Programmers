# 방법1
# def solution(numbers):
#     sum = 0
#     if(len(numbers) >= 1 and len(numbers) <= 100) :
#         for i in range(len(numbers)) :
#             if (numbers[i] >= 0 and numbers[i] <= 1000) :
#                 sum = sum + numbers[i]
#         answer = sum / len(numbers)
#     return answer

# 방법2
import statistics

def solution(numbers):
    
    if(len(numbers) >= 1 and len(numbers) <= 100) :
        for i in range(len(numbers)) :
            if (numbers[i] >= 0 and numbers[i] <= 1000) :
                answer = statistics.mean(numbers)
    return answer
