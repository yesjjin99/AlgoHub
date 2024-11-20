from collections import deque

from Programmers.Level3.네트워크 import find_parent


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)

    def bfs(s, end):
        cnt = 0
        visited = [0] * (n + 1)
        queue = deque([s])
        visited[s] = 1

        while queue:
            v = queue.popleft()
            cnt += 1  # 개수 증가

            for i in graph[v]:
                if i != end and not visited[i]:  # 분할했을 때의 송전탑 개수
                    queue.append(i)
                    visited[i] = 1

        return cnt

    result = []
    for i, j in wires:  # 양쪽의 송전탑 개수 차이(절대값)
        result.append(abs(bfs(i, j) - bfs(j, i)))

    return min(result)

# ---

def find(parent, x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b

def solution(n, wires):
    answer = 1e9

    for w in range(len(wires)):
        parent = [-1] * (n + 1)

        for a, b in wires[:w] + wires[w + 1:]:  # 간선을 하나씩 차례대로 제외해보면서, 그 상태로 union find
            union(parent, a, b)

        cnt1 = parent[find(parent, wires[w][0])]  # 제외한 간선 양 끝 점의 루트 노드 parent 값이 송전탑 개수
        cnt2 = parent[find(parent, wires[w][1])]
        answer = min(answer, abs(cnt1 - cnt2))

    return answer
