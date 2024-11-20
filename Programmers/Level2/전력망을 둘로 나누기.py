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
