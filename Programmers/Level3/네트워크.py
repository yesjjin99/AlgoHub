# DFS
def solution(n, computers):
    count = 0
    visited = [False] * n

    def dfs(v, visited):
        visited[v] = True

        for i in range(len(computers[v])):
            if computers[v][i] == 1 and not visited[i]:
                dfs(i, visited)

    for i in range(n):
        if not visited[i]:  # 한 번도 방문하지 않은 노드라면 count + 1, 해당 노드를 기준으로 DFS 수행!
            dfs(i, visited)
            count += 1

    return count


# BFS
from collections import deque

def solution(n, computers):
    count = 0
    visited = [False] * n

    def bfs(start, visited):
        queue = deque([start])
        visited[start] = True

        while queue:
            v = queue.popleft()

            for i in range(len(computers[v])):
                if computers[v][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    for i in range(n):
        if not visited[i]:
            bfs(i, visited)
            count += 1

    return count


# Union Find
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, computers):
    parents = []

    for i in range(n):
        parents.append(i)

    # 부모 합치기 연산 수행
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_parent(parents, i, j)

    # 부모 테이블이 업데이트되지 않은 경우를 위해 각각의 노드에 대해 부모 찾기 연산 수행
    for i in range(n):
        parents[i] = find_parent(parents, i)
    return len(set(parents))  # 같은 부모라면 같은 네트워크이므로 중복 제외
