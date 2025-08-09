import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
roads = [list(map(int, input().split())) for _ in range(n)]

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if roads[i][j] == 0:
            continue

        union(i + 1, j + 1)

pos = True
plans = list(map(int, input().split()))
for i in range(m - 1):
    if parent[plans[i]] != parent[plans[i + 1]]:
        pos = False
        break

print("YES" if pos else "NO")

# ---

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
roads = [list(map(int, input().split())) for _ in range(n)]
plans = list(map(int, input().split()))

visited = [False] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in range(n):
            if roads[v][i] and not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(plans[0] - 1)
answer = "YES"
for p in plans:
    if not visited[p - 1]:
        answer = "NO"
        break

print(answer)