N, M = map(int, input().split())
answer = [0]*10
isused = [0]*10


def solve(level):
    global N, M
    if level == M:
        for i in range(M): print(answer[i], end=' ')
        print()
        return
    for i in range(1, N+1):
        if isused[i]: continue
        isused[i] = True
        answer[level] = i
        solve(level + 1)
        isused[i] = False

solve(0)
