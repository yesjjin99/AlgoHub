from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():  # 치즈가 없는 부분을 방문 처리하여 외부 공기와 접촉하는지 표시
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] >= 1:  # 치즈인 부분인 경우, 1 더해주기
                    graph[nx][ny] += 1  # 치즈를 만나면 queue에 넣지 않기 때문에 치즈 내부에 있는 좌표로는 이동할 수가 없게 된다
                else:  # 외부 공기인 경우, 방문 처리
                    queue.append((nx, ny))
                    visited[nx][ny] = True


def melt_cheeze():  # 외부 공기와 2변 이상 접촉한 부분을 제거
    melted = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:  # 2번 이상이라면 (기존에 치즈로 표시된 1에서 치즈를 만날 때마다 1씩 더해주었기 때문
                melted += 1
                graph[i][j] = 0  # 해당 위치의 치즈 제거
            elif graph[i][j] >= 2:
                graph[i][j] = 1  # 다시 BFS를 통해 방문하기 위해 초기화
    return melted


answer = 0
while True:
    bfs()
    melted = melt_cheeze()

    if melted:
        answer += 1
    else:
        print(answer)
        break