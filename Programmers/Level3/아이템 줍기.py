from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    grid = [[0] * 102 for _ in range(102)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 직사각형의 외곽, 내부 표시
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda a: a * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if grid[i][j] <= 1:  # 아직 직사각형이 놓이지 않은 위치거나 다른 직사각형의 테두리인 경우
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        grid[i][j] = 1  # 테두리
                    else:
                        grid[i][j] = 2  # 내부

    # ㄷ자의 형태로 테두리가 있을 경우 이대로 BFS를 수행하게 되면 일자로 가게 된다
    # 이를 방지하기 위해 모든 좌표를 2배쌕 해준다
    cx, cy, ix, iy = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY

    # BFS
    visited = [[-1] * 102 for _ in range(102)]
    queue = deque([(cx, cy)])  # 시작접의 위치
    visited[cx][cy] = 0

    while queue:
        x, y = queue.popleft()
        if x == ix and y == iy:
            answer = visited[x][y] // 2  # 좌표를 2배씩 곱해주었기 때문에 이동 거리도 2배만큼 나오므로 나누이 2를 해준다
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if grid[nx][ny] == 1 and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return answer