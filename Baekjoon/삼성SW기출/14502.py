import copy
from collections import deque

n, m = map(int, input().split())
graph, virus = [], []  # 지도, 바이러스 위치
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 2:
            virus.append((i, j))

def make_walls(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1  # 벽 설치
                make_walls(count + 1)
                graph[i][j] = 0

def bfs():
    global answer

    queue = deque(virus)  # 큐에 모든 바이러스 위치 넣어놓기
    maps = copy.deepcopy(graph)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:  # 빈 칸인 경우
                maps[nx][ny] = 2  # 바이러스 퍼뜨기리
                queue.append((nx, ny))

    result = 0
    for tmp in maps:
        result += tmp.count(0)  # 안전 영역 크기 구하기
    answer = max(answer, result)  # 안전 영역의 최대 크기 갱신

make_walls(0)
print(answer)