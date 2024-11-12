def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
x, y, z = [], [], []  # x축, y축, z축 각각에 대하여
for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = []  # 가중치, a 행성, b 행성
for cur in x, y, z:  # min(|xA-xB|, |yA-yB|, |zA-zB|) 를 구해야하므로 x축, y축, z축에서의 최소 비용을 함께 비교
    for i in range(n - 1):
        edges.append((abs(cur[i + 1][0] - cur[i][0]), cur[i][1], cur[i + 1][1]))

edges.sort()

parent = [i for i in range(n)]
result = 0

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
