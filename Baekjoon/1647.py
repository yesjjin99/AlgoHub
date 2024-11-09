import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))  # 유지비, 집 A, 집 B

edges.sort()

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

last = 0  # MST에 포함되는 가장 비용이 큰 간선
for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        last = cost

# 전체 그래프에서 가장 최소한의 비용을 가지는 최소 신장 트리 2개를 만드려면 최소 신장 트리를 구한 후 가장 비용이 큰 간선을 제거하면 된다
print(result - last)
