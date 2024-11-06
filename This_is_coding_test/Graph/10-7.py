import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블

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


for i in range(1, n + 1):
    parent[i] = i  # 부모를 자기 자신으로 초기화

for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:  # 팀 합치기(union)
        union_parent(a, b)
    elif t == 1:  # 같은 팀 여부 확인(find)
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
