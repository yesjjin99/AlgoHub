g = int(input())
p = int(input())

parent = [0] * (g + 1)
for i in range(1, g + 1):
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

count = 0
for _ in range(p):
    gi = int(input())
    data = find_parent(gi)  # 현재 비행기의 탑승구 루트 확인
    if data == 0:  # 루트가 0이라면 종료
        break

    count += 1
    union_parent(data, data - 1)  # 왼쪽의 집합과 union

print(count)
