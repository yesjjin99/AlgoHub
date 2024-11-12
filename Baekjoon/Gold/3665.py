from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    score = list(map(int, input().split()))
    m = int(input())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for i in range(n + 1)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[score[i]][score[j]] = True
            indegree[score[j]] += 1

    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1


    # 위상 정렬
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True  # 위상 정렬 결과가 오직 하나인지
    cycle = False  # 그래프 내 사이클이 존재하는지

    for _ in range(n):  # 노드의 개수만큼 반복
        if len(q) == 0:  # 모든 원소를 방문하기 전에 큐가 비어있다면 사이클이 발생한 것
            cycle = True
            break
        if len(q) >= 2:  # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n + 1):  # 해당 원소와 연결된 노드들의 진입차수 1씩 빼기
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:  # 사이클이 발생한 경우 -> IMPOSSIBLE
        print("IMPOSSIBLE")
    elif not certain:  # 위상 정렬 결과가 여러 개인 경우 -> ?
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()
