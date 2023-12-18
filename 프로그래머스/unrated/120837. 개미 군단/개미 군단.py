def solution(hp):
    if (hp >= 0 and hp <= 1000) :
        b_ant = hp // 5 
        m_ant = (hp % 5) // 3
        s_ant = (hp % 5) % 3
    return b_ant + m_ant + s_ant