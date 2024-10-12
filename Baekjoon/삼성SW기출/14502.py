import copy
from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
result = 0
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0],

def bfs():  # 바이러스 퍼트리고 안전영역 계산
    global result
    queue = deque()
    temp = copy.deepcopy(maps)  # 백트래킹을 위한 확인용 map
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))

    count = 0
    for t in temp:
        count += t.count(0)
    result = max(result, count)

def make_wall(empty):  # 벽 세우기
    if empty == 3:
        bfs()  # 바이러스 퍼트리기
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:  # 빈 공간이라면 벽 세우기 가능
                maps[i][j] = 1  # 벽 세우기
                make_wall(empty + 1)  # 다시 다음 벽 세우러 가기
                maps[i][j] = 0  # 다시 벽 허물기 (백트래킹)


make_wall(0)
print(result)
