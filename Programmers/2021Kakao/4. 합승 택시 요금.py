import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for b, c in graph[now]:
                cost = dist + c
                if cost < distance[b]:
                    heapq.heappush(q, (cost, b))
                    distance[b] = cost

        return distance


    dist = [0] + [dijkstra(i) for i in range(1, n + 1)]

    answer = INF
    for k in range(1, n + 1):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])

    return answer