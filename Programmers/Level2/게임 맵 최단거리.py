from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque([(0, 0)])

    while queue:  # BFS
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1  # 방문 처리 및 카운트 증가

    # BFS 에서 가장 처음 도달하는 경우가 최단거리
    return maps[n - 1][m - 1] if maps[n - 1][m - 1] != 1 else -1
