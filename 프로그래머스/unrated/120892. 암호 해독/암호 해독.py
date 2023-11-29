def solution(cipher, code):
    secret = ''
    if(len(cipher) >= 1 and len(cipher) <= 1000 and code >= 1 and code <= len(cipher)) :
        for i in range(1, len(cipher) + 1) :
            if i % code == 0 :
                secret = secret + cipher[i-1]
    return secret