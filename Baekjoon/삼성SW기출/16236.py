from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:  # 아기 상어의 위치
            x, y = i, j

def bfs(x, y, size):  # 현재 아기 상어의 위치에서 어디로 이동할지(어느 칸에 있는 물고기를 먹을지) 결정
    queue = deque([(x, y)])
    visited = [[0] * n for _ in range(n)]
    fishes = []  # 먹을 수 있는 물고기들

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] <= size:  # 자신의 크기보다 큰 물고기가 있는 칸을 제외한 모든 칸 탐색
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1  # 해당 칸까지의 이동 시간

                if board[nx][ny] != 0 and board[nx][ny] < size:  # 아기 상어의 크기보다 작은 물고기가 있는 칸 (먹을 수 있는 물고기 칸)
                    fishes.append((nx, ny, visited[nx][ny]))  # 물고기의 위치, 물고기가 있는 칸까지 이동한 시간

    return sorted(fishes, key=lambda x: (x[2], x[0], x[1]))

result, size, count = 0, 2, 0

while True:
    fishes = bfs(x, y, size)

    if len(fishes) == 0:  # 더 이상 먹을 물고기가 존재하지 않는 경우
        print(result)
        break

    nx, ny, time = fishes[0]
    result += time
    board[x][y], board[nx][ny] = 0, 0  # 아기 상어의 위치와 물고기의 위치 0으로 초기화
    x, y = nx, ny  # 아기 상어의 위치 이동
    count += 1

    if count == size:  # 아기 상어의 크기만큼 물고기를 먹은 경우
        size += 1
        count = 0