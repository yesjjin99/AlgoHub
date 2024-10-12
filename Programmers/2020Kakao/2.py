# 괄호 변환
def check(p):
    cnt = 0
    for c in p:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break

    return cnt == 0


def divide(p):
    cnt = 0
    for i, c in enumerate(p):
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return p[:i + 1], p[i + 1:]


def solution(p):
    if not p:
        return p

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        temp = '(' + solution(v) + ')'
        for s in u[1:-1]:
            if s == '(':
                temp += ')'
            else:
                temp += '('
        return temp
