import heapq
INF = int(1e9)

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    def dijkstra(start):  # 최단경로
        hq = []
        heapq.heappush(hq, (0, start))  # 시작 노드
        distance[start] = 0

        while hq:
            dist, now = heapq.heappop(hq)  # 가장 최단 거리가 짧은 노드
            if distance[now] < dist:  # 이미 더 짧은 노드를 찾은 경우라면
                continue

            for i in graph[now]:
                cost = dist + 1
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(hq, (cost, i))

    dijkstra(1)

    distance.sort(reverse=True)
    return distance[1:].count(distance[1])  # 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지