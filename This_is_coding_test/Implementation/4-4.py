# 시뮬레이션
n, m = map(int, input().split())
x, y, d = map(int, input().split())
map = []
for _ in range(n):
    map.append(input().split())

count, turn = 1, 0  # 방문한 칸의 수, 회전 횟수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

map[x][y] = 2  # 현재 위치 방문 처리
while True:
    d = (d + 3) % 4  # 왼쪽으로 회전
    nx, ny = x + dx[d], y + dy[d]
    if map[nx][ny] == 0:
        map[nx][ny] = 2  # 방문 처리
        x, y = nx, ny  # 이동
        count += 1
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        nx, ny = x - dx[d], y - dy[d]
        if map[nx][ny] != 1:
            x, y = nx, ny
            turn = 0
        else:
            break

print(count)
