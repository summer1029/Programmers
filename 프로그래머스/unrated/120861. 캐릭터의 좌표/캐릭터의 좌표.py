def solution(keyinput, board):
    x = 0
    y = 0
    for command in keyinput :
        if command == "up" :
            x = x
            y = y + 1
            if y > board[1] // 2 :
                y = y - 1
        if command == "down" :
            x = x
            y = y - 1
            if abs(y) > board[1] // 2 :
                y = y + 1
        if command == "left" :
            x = x - 1
            if abs(x) > board[0] // 2 :
                x = x + 1
            y = y
        if command == "right" :
            x = x + 1
            if abs(x) > board[0] // 2 :
                x = x - 1
            y = y
    return [x, y]