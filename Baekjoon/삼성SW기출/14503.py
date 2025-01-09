from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]  # 0은 빈 칸, 1은 벽

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 0: 북, 1: 동, 2: 남, 3: 서

def bfs(x, y, d):
    queue = deque([(x, y)])
    room[x][y] = 2  # 청소된 상태
    cnt = 1

    while queue:
        x, y = queue.popleft()
        empty = 0  # 청소되지 않은 빈 칸의 개수

        for _ in range(4):
            d = (d + 3) % 4  # 반시계 방향으로 90도 회전
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
                queue.append((nx, ny))
                room[nx][ny] = 2
                empty += 1
                cnt += 1
                break

        if empty == 0:  # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            nx, ny = x - dx[d], y - dy[d]  # 한 칸 후진
            if room[nx][ny] == 1:  # 벽이라 후진할 수 없다면 작동을 멈춘다
                return cnt
            else:
                queue.append((nx, ny))

print(bfs(r, c, d))