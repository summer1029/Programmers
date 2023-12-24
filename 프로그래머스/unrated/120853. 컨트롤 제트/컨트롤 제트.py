def solution(s):
    if len(s) >= 1 and len(s) <= 200 :
        split_s = s.split(" ")
        sum = int(split_s[0])
        for idx in range(1, len(split_s)) :
            if split_s[idx] == 'Z' :
                sum = sum - int(split_s[idx - 1])
            else :
                sum = sum + int(split_s[idx])
        return sum