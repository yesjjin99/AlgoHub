import copy

n, m = map(int, input().split())
graph, cameras = [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] in [1, 2, 3, 4, 5]:
            cameras.append((tmp[j], i, j))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
mode = [  # CCTV 별 방향 정보
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [0, 3], [1, 2], [1, 3]],
    [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
    [[0, 1, 2, 3]]
]

def fill(x, y, mode, graph):  # 상, 하, 좌, 우로 현재 CCTV가 감시할 수 있는 영역
    for i in mode:
        nx, ny = x, y
        while True:
            nx, ny = nx + dx[i], ny + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 6:  # 범위를 벗어났거나 벽인 경우
                break
            if graph[nx][ny] == 0:  # 빈 칸인 경우 -> 즉, 이미 CCTV가 감시한 영역이 아닌 경우
                graph[nx][ny] = -1

def dfs(count, graph):  # 각 CCTV 별로 가장 최적의 방향 조합 찾기
    global result

    if count == len(cameras):
        total = 0
        for i in range(n):
            total += graph[i].count(0)

        result = min(result, total)  # 최소값 갱신
        return

    tmp = copy.deepcopy(graph)
    cctv_num, x, y = cameras[count]
    for m in mode[cctv_num]:
        fill(x, y, m, tmp)  # 감시 시작
        dfs(count + 1, tmp)
        tmp = copy.deepcopy(graph)  # 그래프 초기화

result = int(1e9)
dfs(0, graph)
print(result)