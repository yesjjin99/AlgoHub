def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return len(stack) == 0


def solution(s):
    cnt = 0
    for c in s:
        if c == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            else:
                cnt -= 1
    return cnt == 0
