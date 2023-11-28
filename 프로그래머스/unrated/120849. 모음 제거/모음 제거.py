def solution(my_string):
    vowel = "aeiou"
    if (len(my_string) >= 1 and len(my_string) <= 1000) :
        for char in my_string :
            if char in vowel :
                my_string = my_string.replace(char, '')
    return my_string