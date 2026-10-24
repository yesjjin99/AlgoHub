import heapq
INF = int(1e9)

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 다익스트라 (최단 경로)
    # 1번 마을에서 각 마을까지의 최소 비용 구하기
    q = []
    heapq.heappush(q, (0, 1))  # 1번 마을에서 출발
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

    # K 시간 이하인 마을의 개수 집계
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1

    return answer