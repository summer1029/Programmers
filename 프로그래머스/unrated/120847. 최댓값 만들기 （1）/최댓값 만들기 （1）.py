def solution(numbers):
    first = 0
    second = 0
    
    if (len(numbers) >= 2 and len(numbers) <= 100) :
        for i in range(len(numbers)) :
            if (numbers[i] >= 0 and numbers[i] <= 10000) :
                if (numbers[i] > first) : # 원소가 first보다 더 크면
                    second = first # second에 first원소를 넣고
                    first = numbers[i] # first에 이보다 더 큰 원소를 넣는다
                elif (second < numbers[i] <= first) : # 원소가 first보단 작으나 second보다 크면 
                    second = numbers[i] # second만 갱신한다
                        
        answer = first * second
    return answer