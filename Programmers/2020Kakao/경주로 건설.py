from collections import deque

def solution(board):  # 0은 칸이 비어 있음, 1은 칸이 벽으로 채워져 있음
    n = len(board)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 경주로 건설 - 직선 도로 100원, 코너 500원
    def bfs(x, y, cost, d):
        queue = deque([(x, y, cost, d)])
        visited = [[int(1e9)] * n for _ in range(n)]
        visited[x][y] = 0

        while queue:
            x, y, cost, d = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
                    continue

                if d == i: ncost = cost + 100
                else: ncost = cost + 600

                if ncost < visited[nx][ny]:  # 최소 비용이면 갱신 후, enqueue
                    queue.append((nx, ny, ncost, i))
                    visited[nx][ny] = ncost

        return visited[n - 1][n - 1]

    return min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 3))  # (0, 0)에서는 동쪽 혹은 남쪽으로만 이동 가능