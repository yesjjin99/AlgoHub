N, M = map(int, input().split())
answer = [0]*10


def solve(level, num):
    global N, M
    if level == M:
        for i in range(M): print(answer[i], end=' ')
        print()
        return
    for i in range(num, N+1):
        answer[level] = i
        solve(level + 1, i + 1)


solve(0, 1)
