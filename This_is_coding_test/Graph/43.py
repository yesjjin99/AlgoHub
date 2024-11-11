import sys
# input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []  # 모든 도로의 정보를 담을 리스트
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))  # 비용이 첫 번째 원소

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


edges.sort()

for z, x, y in edges:
    if find_parent(x) != find_parent(y):  # 사이클이 발생하지 않을 때만 포함
        union_parent(x, y)
    else:
        result += z

print(result)  # 절약할 수 있는 최대 금액
