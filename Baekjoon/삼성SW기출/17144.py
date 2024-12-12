r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
for i in range(r):
    if room[i][0] == -1:
        air = i
        break


def diffuse():
    diffusion = [[0] * c for _ in range(r)]  # 각 위치마다 확산되는 미세먼지 양

    for x in range(r):
        for y in range(c):
            if room[x][y] == 0 or room[x][y] == -1:
                continue

            amount = room[x][y] // 5
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or room[nx][ny] == -1:
                    continue
                diffusion[nx][ny] += amount
                cnt += 1

            room[x][y] -= cnt * amount

    for i in range(r):  # 미세먼지 양 계산
        for j in range(c):
            room[i][j] += diffusion[i][j]


def rotate():
    # 위쪽 반시계 방향
    for i in range(air - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    for j in range(c - 1):
        room[0][j] = room[0][j + 1]
    for i in range(air):
        room[i][-1] = room[i + 1][-1]
    for j in range(c - 1, 0, -1):
        room[air][j] = room[air][j - 1]
    room[air][1] = 0

    # 아래쪽 시계 방향
    for i in range(air + 2, r - 1):
        room[i][0] = room[i + 1][0]
    for j in range(c - 1):
        room[-1][j] = room[-1][j + 1]
    for i in range(r - 1, air + 1, -1):
        room[i][-1] = room[i - 1][-1]
    for j in range(c - 1, 0, -1):
        room[air + 1][j] = room[air + 1][j - 1]
    room[air + 1][1] = 0

for _ in range(t):
    diffuse()
    rotate()

result = 0
for row in room:
    result += sum(row)
print(result + 2)  # 공기 청정기 제외
