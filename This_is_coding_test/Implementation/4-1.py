# 시뮬레이션
n = int(input())
routes = input().split()

x, y = 1, 1
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D']

for route in routes:
    for i in range(4):
        if route == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
