import copy
from collections import deque
INF = int(1e9)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # 0은 빈 칸, 1은 벽, 2는 비활성 바이러스
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

answer = INF
candidate = []
empty_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            candidate.append((i, j, 0))
        elif graph[i][j] == 0:
            empty_cnt += 1


def activate_virus(select, idx):
    if len(select) == m:  # 바이러스 M개를 활성 상태로 변경한 경우
        bfs(select)
        return

    for i in range(idx, len(candidate)):
        select.append(candidate[i])
        activate_virus(select, i + 1)
        select.remove(candidate[i])


def bfs(select):
    global answer

    max_time = 0
    virus_count = 0
    temp_lab = copy.deepcopy(graph)
    queue = deque(select)

    # bfs를 위한 반복
    while queue:
        x, y, time = queue.popleft()
        # 활성된 바이러스는 3으로 표시
        temp_lab[x][y] = 3

        # 빈칸이 모두 채워진 경우에
        if virus_count == empty_cnt:
            answer = min(answer, max_time)
            return

        # 연산시간 단축을 위해 현재 시간이 최소 시간 이상이면 리턴
        if time >= answer:
            return

        # 모든 방향에 대하여
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 범위 이내인경우에
            if 0 <= nx < n and 0 <= ny < n:
                # 빈칸이면 확산, 확산된 수를 체크
                if temp_lab[nx][ny] == 0:
                    virus_count += 1
                    temp_lab[nx][ny] = 3
                    queue.append([nx, ny, time + 1])
                    max_time = time + 1
                # 비활성 바이러스를 만나면 활성 바이러스로
                elif temp_lab[nx][ny] == 2:
                    temp_lab[nx][ny] = 3
                    queue.append([nx, ny, time + 1])

activate_virus([], 0)
print(-1 if answer == INF else answer)