def solution(age):
    if age >= 0 and age <= 120:
        year = 2022
        for i in range(1, age) :
            year = year - 1
    return year