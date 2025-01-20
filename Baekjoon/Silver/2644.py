n = int(input())
p1, p2 = map(int, input().split())
rel = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    x, y = map(int, input().split())  # 부모, 자식
    rel[x].append(y)
    rel[y].append(x)

result = 0
visited = [0] * (n + 1)
def dfs(v, cnt):
    global result

    visited[v] = 1
    if v == p2:
        result = cnt
        return

    for r in rel[v]:
        if not visited[r]:
            dfs(r, cnt + 1)

dfs(p1, 0)
print(result if result else -1)