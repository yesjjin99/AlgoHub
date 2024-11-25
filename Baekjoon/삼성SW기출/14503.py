from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]  # 0이면 빈 칸, 1이면 벽

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북, 동, 남, 서

def bfs(x, y, d):
    q = deque([(x, y)])
    room[x][y] = 2
    count = 1

    while q:
        x, y = q.popleft()
        isEmpty = True
        for _ in range(4):
            d = (d + 3) % 4  # 회전
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:  # 청소되지 않은 빈 칸인 경우
                q.append((nx, ny))
                room[nx][ny] = 2  # 현재 칸 청소
                count += 1
                isEmpty = False
                break

        if isEmpty:  # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없다면
            nx, ny = x - dx[d], y - dy[d]  # 후진
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if room[nx][ny] == 1:  # 벽이라면
                return count
            else:
                q.append((nx, ny))

print(bfs(r, c, d))
