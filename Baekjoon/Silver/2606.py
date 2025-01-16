from collections import deque

n = int(input())
coms = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)

def bfs(v):
    result = 0
    queue = deque([v])
    visited = [0] * (n + 1)
    visited[v] = 1

    while queue:
        v = queue.popleft()
        for i in coms[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                result += 1

    return result

print(bfs(1))