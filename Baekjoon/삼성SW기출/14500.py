n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

def dfs(x, y, count, total, visited):  # ㅗ 모양을 제외한 테트로미노 탐색
    global answer

    if count == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, count + 1, total + graph[nx][ny], visited)
            visited[nx][ny] = 0

def find(x, y):  # ㅗ 모양 테트로미노 탐색 (DFS 로 나올 수 없는 모양)
    global answer

    arr = []
    for i in range(4):  # ㅗ 모양을 만들기 위해 4방향 모두 추가
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            arr.append(graph[nx][ny])

    if len(arr) == 4:  # 만약 4방향 모두 추가된다면, 그 중 가장 작은 값 제거 후 sum
        answer = max(answer, graph[x][y] + sum(arr) - min(arr))
    elif len(arr) == 3:  # 만약 3방향만 추가된다면, 바로 sum
        answer = max(answer, graph[x][y] + sum(arr))

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):  # 모든 칸을 시작점으로 탐색
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j], visited)
        find(i, j)
        visited[i][j] = 0

print(answer)