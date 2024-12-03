import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]  # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
cx, cy = [-1, -1, 1, 1], [-1, 1, -1, 1]  # 대각선 방향

clouds = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]  # 비바라기 시전

for _ in range(m):
    visited = [[False] * n for _ in range(n)]

    d, s = map(int, input().split())
    for i, (x, y) in enumerate(clouds):
        nx = (x + dx[d - 1] * s) % n
        ny = (y + dy[d - 1] * s) % n
        # nx, ny = x + dx[d - 1] * s, y + dy[d - 1] * s
        # if nx < 0:  # 1번 행과 N번 행을 연결
        #     nx = -(-nx % n)
        #     if nx != 0:
        #         nx += n
        # elif nx >= n:
        #     nx %= n
        # if ny < 0:  # 1번 열과 N번 열도 연결
        #     ny = -(-ny % n)
        #     if ny != 0:
        #         ny += n
        # elif ny >= n:
        #     ny %= n

        clouds[i] = (nx, ny)
        arr[nx][ny] += 1
        visited[nx][ny] = True

    for i, (x, y) in enumerate(clouds):
        cnt = 0
        for j in range(4):
            nx, ny = x + cx[j], y + cy[j]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                cnt += 1
        arr[x][y] += cnt

    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and not visited[i][j]:
                tmp.append((i, j))
                arr[i][j] -= 2
    clouds = tmp

print(sum(sum(a) for a in arr))
