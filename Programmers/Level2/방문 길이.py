def solution(dirs):
    move = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    visited = set()

    x, y = 0, 0
    for d in dirs:
        nx, ny = x + move[d][0], y + move[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add(((x, y), (nx, ny)))
            visited.add(((nx, ny), (x, y)))
            x, y = nx, ny
    return len(visited) // 2


# ---


from collections import deque

dx = {"U": 0, "D": 0, "R": 1, "L": -1}
dy = {"U": 1, "D": -1, "R": 0, "L": 0}


def solution(dirs):
    answer = 0
    visited = [[{"U": False, "D": False, "R": False, "L": -False} for _ in range(11)] for _ in
               range(11)]  # 각 좌표에서 U, D, R, L 방향으로 이어진 길의 방문 여부

    # BFS
    queue = deque([(5, 5)])  # x좌표, y좌표
    c = 0  # 이동 횟수

    while queue:
        x, y = queue.popleft()

        if c == len(dirs): break

        nx, ny = x + dx[dirs[c]], y + dy[dirs[c]]  # 이동
        if nx < 0 or nx > 10 or ny < 0 or ny > 10:
            queue.append((x, y))
            c += 1
            continue  # 좌표평면의 경계를 넘어가는 명령어는 무시

        if not visited[x][y][dirs[c]]:
            answer += 1

        queue.append((nx, ny))
        visited[x][y][dirs[c]] = True
        visited[nx][ny][change_dir(dirs[c])] = True
        c += 1

    return answer


def change_dir(d):
    result = ""

    if d == "U":
        result = "D"
    elif d == "D":
        result = "U"
    elif d == "R":
        result = "L"
    elif d == "L":
        result = "R"

    return result
