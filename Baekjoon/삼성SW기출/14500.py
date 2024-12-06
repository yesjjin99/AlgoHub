n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

result = 0
def dfs(x, y, total, count, visited):  # ㅗ 모양을 제외한 나머지 모양 탐색
    global result

    if count == 4:
        result = max(result, total)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, total + graph[nx][ny], count + 1, visited)
            visited[nx][ny] = 0

def find(x, y):  # ㅗ 모양 탐색 (DFS로 나올 수 없는 모양임)
    global result

    arr = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            arr.append(graph[nx][ny])

    if len(arr) == 4:  # 만약 4방향 모두 추가된다면, 그 중 가장 작은 값 제거 후 sum
        arr.sort(reverse=True)
        arr.pop()
        result = max(result, sum(arr) + graph[x][y])
    elif len(arr) == 3:  # 만약 3방향만 추가된다면, 바로 sum
        result = max(result, sum(arr) + graph[x][y])


visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, graph[i][j], 1, visited)
        find(i, j)
        visited[i][j] = 0
print(result)
