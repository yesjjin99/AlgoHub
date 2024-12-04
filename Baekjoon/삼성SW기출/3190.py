from collections import deque

n = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1  # 사과의 위치
dir_change = deque([list(input().split()) for _ in range(int(input()))])
time = 0

snake = deque([(0, 0)])
graph[0][0] = 2  # 뱀의 위치
dir = (0, 1)  # 오른쪽 방향
while True:
    time += 1
    nx, ny = snake[0][0] + dir[0], snake[0][1] + dir[1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:  # 벽이나 자기자신의 몸과 부딪히면 게임 끝
        break

    snake.appendleft((nx, ny))  # 몸길이를 늘려 머리를 다음칸에 위치
    if graph[nx][ny] == 0:  # 이동한 칸에 사과가 없다면
        a, b = snake.pop()  # 꼬리가 위치한 칸을 비워준다
        graph[a][b] = 0
    graph[nx][ny] = 2

    if dir_change and time == int(dir_change[0][0]):  # 방향 변환
        x, y = dir
        if dir_change[0][1] == 'L':
            if x == 0:
                dir = (-y, x)
            elif y == 0:
                dir = (y, x)
        elif dir_change[0][1] == 'D':
            if x == 0:
                dir = (y, x)
            elif y == 0:
                dir = (y, -x)
        dir_change.popleft()

print(time)
