import copy
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
answer = 0

def bfs():
    global answer
    queue = deque()
    temp = copy.deepcopy(maps)  # 백트래킹을 위한 확인용 map

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:  # 바이러스가 존재하는 칸
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2  # 바이러스 퍼뜨리기
                queue.append((nx, ny))

    result = 0
    for x in range(n):
        result += temp[x].count(0)
    answer = max(answer, result)


def make_walls(cnt):
    if cnt == 3:
        bfs()  # 바이러스 퍼트리기
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:  # 빈 공간이라면 벽 세우기 가능
                maps[i][j] = 1  # 벽 세우기
                make_walls(cnt + 1)  # 다시 다음 벽 세우러 가기
                maps[i][j] = 0  # 다시 벽 허물기 (백트래킹)

make_walls(0)
print(answer)
