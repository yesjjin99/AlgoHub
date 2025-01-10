# 블록 이동하기
from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과 (이동 가능한 위치들)
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    # 이동
    for i in range(4):
        nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:  # 이동 가능하다면
            next_pos.append({(nx1, ny1), (nx2, ny2)})

    # 회전
    if x1 == x2:  # 로봇이 가로로 있다면
        for i in [-1, 1]:  # 위, 아래로 회전
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:  # 대각선과 이동할 칸이 모두 빈칸이라면
                next_pos.append({(x1, y1), (x1 + i, y1)})  # 축을 왼쪽으로 할지, 오른쪽으로 할지에 따라 다르게 회전
                next_pos.append({(x2, y2), (x2 + i, y2)})

    elif y1 == y2:  # 로봇이 세로로 있다면
        for i in [-1, 1]:  # 왼쪽, 오른쪽 회전
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append({(x1, y1), (x1, y1 + i)})
                next_pos.append({(x2, y2), (x2, y2 + i)})

    return next_pos

def solution(board):
    n = len(board)
    # 범위판정을 수월하게 하기 위해 기존 맵의 외곽에 벽을 두는 형태로 변형
    new_board = [[1] * (n + 2) for _ in range(n + 2)]  # 맵 변형하지 않고 범위체크하면 시간초과 뜸
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):  # 현재 위치에서 이동할 수 있는 모든 경우
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
