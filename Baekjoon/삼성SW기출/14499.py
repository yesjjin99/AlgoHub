n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]  # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dice = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}  # 주사위 각 면의 반대 면
value = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # 주사위 각 면의 값
pos = [6, 2, 3]  # 바닥면, 남쪽, 동쪽 (주사위의 처음 시작은 윗면이 1, 동쪽이 3)

for move in moves:
    nx, ny = x + dx[move - 1], y + dy[move - 1]  # 좌표 이동
    if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 지도의 바깥으로 이동이라면 무시
        continue

    x, y = nx, ny
    a, b, c = pos  # 바닥면, 남쪽, 동쪽
    if move == 1:  # 주사위 회전
        pos = [c, b, dice[a]]
    elif move == 2:
        pos = [dice[c], b, a]
    elif move == 3:
        pos = [dice[b], a, c]
    elif move == 4:
        pos = [b, dice[a], c]

    if graph[x][y] == 0:  # 이동한 칸에 쓰여 있는 수가 0
        graph[x][y] = value[pos[0]]  # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    else:
        value[pos[0]] = graph[x][y]  # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
        graph[x][y] = 0  # 칸에 쓰여 있는 수는 0이 된다

    print(value[dice[pos[0]]])  # 이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력
