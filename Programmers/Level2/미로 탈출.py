from collections import deque

def solution(maps):
    maps = [list(m) for m in maps]
    sx, sy, ex, ey, lx, ly = 0, 0, 0, 0, 0, 0  # 시작 지점, 출구, 레버
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                sx, sy = i, j
                maps[i][j] = 'O'
            elif maps[i][j] == 'E':
                ex, ey = i, j
                maps[i][j] = 'O'
            elif maps[i][j] == 'L':
                lx, ly = i, j
                maps[i][j] = 'O'

    def bfs(x, y, tx, ty):
        queue = deque([(x, y)])
        visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = 0

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] == 'O' and visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

        return visited[tx][ty]

    l = bfs(sx, sy, lx, ly)
    e = bfs(lx, ly, ex, ey)

    return -1 if l == -1 or e == -1 else l + e