import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    distance = [[INF] * n for _ in range(n)]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(n):
        graph.append(list(map(int, input().split())))

    x, y = 0, 0  # 시작 위치
    q = [(graph[x][y], x, y)]  # 비용, 출발 지점, 목표 지점
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):  # 상하좌우 이동
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])
