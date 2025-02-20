from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]
dc = []  # 뱀의 방향 변환
for _ in range(int(input())):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1  # 사과의 위치
for _ in range(int(input())):
    x, c = input().split()
    dc.append([int(x), c])

def dir_change(dx, dy, c):  # 방향 회전 함수
    if dx == 0:
        if c == 'L':  # 왼쪽으로 회전
            return -dy, -dx
        elif c == 'D':  # 오른쪽으로 회전
            return dy, dx
    elif dy == 0:
        if c == 'L':
            return dy, dx
        elif c == 'D':
            return -dy, -dx

def bfs(x, y):
    queue = deque([(x, y)])
    snake = deque([(x, y)])  # 현재 뱀이 위치해 있는 모든 칸
    dx, dy = 0, 1  # 뱀은 처음에 오른쪽을 향한다
    count = 0  # 시간

    while queue:
        count += 1
        x, y = queue.popleft()
        nx, ny = x + dx, y + dy  # 이동
        if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
            return count  # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다

        queue.append((nx, ny))
        snake.append((nx, ny))

        if board[nx][ny] == 1:  # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다
            board[nx][ny] = 0
        else:
            snake.popleft()  # 꼬리가 위치한 칸 비워주기

        if dc and dc[0][0] == count:
            dx, dy = dir_change(dx, dy, dc[0][1])  # 방향 변환
            dc.pop(0)

print(bfs(0, 0))