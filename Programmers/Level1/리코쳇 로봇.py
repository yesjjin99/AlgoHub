from collections import deque


def solution(board):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    queue = deque()
    visited = [[0] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
                visited[i][j] = 1

    while queue:
        x, y, cnt = queue.popleft();

        if board[x][y] == 'G':
            return cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != 'D':
                nx += dx[i]
                ny += dy[i]

            nx -= dx[i]
            ny -= dy[i]

            if visited[nx][ny] or (nx == x and ny == y):
                continue
            queue.append((nx, ny, cnt + 1))
            visited[nx][ny] = 1

    return -1
