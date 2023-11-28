def solution(my_string, letter):
    if (len(my_string) >= 1 and len(my_string) <= 100) :
        if (len(letter) == 1 and letter in my_string) :
            my_string = my_string.replace(letter, '')
    return my_string

