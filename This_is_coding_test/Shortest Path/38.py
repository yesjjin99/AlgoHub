import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1  # A 학생이 B 학생보다 성적이 낮다 -> 성적 비교 가능

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:  # i에서 j로 도달이 가능하거나 j에서 i로 도달이 가능하면 성적 비교 가능
            cnt += 1
    if cnt == n:  # 모든 학생과 비교하여 자신의 성적 비교가 가능하다면
        result += 1

print(result)
