import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, q = map(int, input().split())
len_board = 2 ** n
board = [list(map(int, input().split())) for _ in range(len_board)]
level = list(map(int, input().split()))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def rotate_melting(board, l):
    result = [[0] * len_board for _ in range(len_board)]
    size = 2 ** l

    # 90도 회전
    for x in range(0, len_board, size):
        for y in range(0, len_board, size):
            for i in range(size):
                for j in range(size):
                    result[j + x][size - i - 1 + y] = board[i + x][j + y]

    # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다
    board = result
    melting = []  # 녹을 얼음 좌표
    for x in range(len_board):
        for y in range(len_board):
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= len_board or ny < 0 or ny >= len_board:
                    continue
                if board[nx][ny] > 0:  # 얼음이 있는 칸
                    cnt += 1

            if board[x][y] != 0 and cnt < 3:  # 얼음이 1 줄어야 하므로 얼음 양이 0이 아니어야 함
                melting.append((x, y))

    for x, y in melting:
        board[x][y] -= 1

    return board

def bfs(board):
    visited = [[False] * len_board for _ in range(len_board)]
    total = 0  # 얼음 총 합
    max_count = 0  # 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수

    for i in range(len_board):
        for j in range(len_board):
            count = 0
            if visited[i][j] or board[i][j] == 0:  # 이미 방문했거나 얼음이 없는 칸이라면 pass
                continue

            # BFS를 통해 얼음 덩어리 탐색
            queue = deque([(i, j)])  # 시작점
            visited[i][j] = True

            while queue:
                x, y = queue.popleft()
                total += board[x][y]
                count += 1

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx < 0 or nx >= len_board or ny < 0 or ny >= len_board:
                        continue

                    if board[nx][ny] != 0 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

            max_count = max(max_count, count)

    print(total)
    print(max_count)

for l in level:
    board = rotate_melting(board, l)
bfs(board)
