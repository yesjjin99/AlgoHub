from collections import deque

n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1
l = int(input())
turn = deque()
for _ in range(l):
    turn.append(input().split())

d = [0, 1]
body = [[0] * n for _ in range(n)]
time = 0
queue = deque([(0, 0)])
body[0][0] = 1

while queue:
    time += 1
    nx, ny = queue[-1][0] + d[0], queue[-1][1] + d[1]  # 한 칸 이동
    if nx < 0 or nx >= n or ny < 0 or ny >= n or body[nx][ny] == 1:
        break

    queue.append((nx, ny))
    body[nx][ny] = 1
    if board[nx][ny] == 1:  # 사과가 있다면
        board[nx][ny] = 0
    else:  # 사과가 없다면
        a, b = queue.popleft()  # 꼬리 비우기
        body[a][b] = 0

    if turn and int(turn[0][0]) == time:  # 방향 전환
        _, c = turn.popleft()
        if d == [0, 1]:
            d = [-1, 0]
        elif d == [0, -1]:
            d = [1, 0]
        elif d == [-1, 0]:
            d = [0, -1]
        elif d == [1, 0]:
            d = [0, 1]

        if c == 'D':
            d[0] *= -1
            d[1] *= -1


print(time)
