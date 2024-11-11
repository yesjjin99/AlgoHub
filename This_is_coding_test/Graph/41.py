n, m = map(int, input().split())
roads = []
for _ in range(n):
    roads.append(list(map(int, input().split())))

travel = list(map(int, input().split()))
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i


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


for i in range(n):
    for j in range(n):
        if roads[i][j] == 1:
            union_parent(i + 1, j + 1)

result = True
for i in range(len(travel) - 1):
    if find_parent(travel[i]) != find_parent(travel[i + 1]):
        result = False
        break

print("YES") if result else print("NO")
