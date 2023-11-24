import math

def solution(num1, num2):
if (num1 > 0 and num1 <= 100 and num2 > 0 and num2 <= 100) :
answer = math.trunc(num1 / num2 * 1000)
return answer
