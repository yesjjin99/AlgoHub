from collections import deque

def solution(maze):
    answer = int(1e9)
    rx, ry, bx, by = 0, 0, 0, 0
    red_visited = [[False] * (len(maze[0])) for _ in range(len(maze))]
    blue_visited = [[False] * (len(maze[0])) for _ in range(len(maze))]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                rx, ry = i, j
                red_visited[i][j] = True
            elif maze[i][j] == 2:
                bx, by = i, j
                blue_visited[i][j] = True


    # BFS
    queue = deque([(rx, ry, bx, by, red_visited, blue_visited, 0)])

    while queue:
        rx, ry, bx, by, red_visited, blue_visited, cnt = queue.popleft()

        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            answer = min(answer, cnt)
            continue

        # 빨강만 먼저 도착한 경우
        if maze[rx][ry] == 3:
            for i in range(4):
                _bx, _by = bx + dx[i], by + dy[i]
                if check(_bx, _by, blue_visited, maze) and (rx, ry) != (_bx, _by):
                    rv = [v[:] for v in red_visited]
                    bv = [v[:] for v in blue_visited]
                    bv[_bx][_by] = True
                    queue.append((rx, ry, _bx, _by, rv, bv, cnt + 1))

        # 파랑만 먼저 도착한 경우
        elif maze[bx][by] == 4:
            for i in range(4):
                _rx, _ry = rx + dx[i], ry + dy[i]
                if check(_rx, _ry, red_visited, maze) and (_rx, _ry) != (bx, by):
                    rv = [v[:] for v in red_visited]
                    bv = [v[:] for v in blue_visited]
                    rv[_rx][_ry] = True
                    queue.append((_rx, _ry, bx, by, rv, bv, cnt + 1))

        # 둘다 도착하지 못한 경우
        else:
            for red_idx in range(4):
                _rx, _ry = rx + dx[red_idx], ry + dy[red_idx]
                if check(_rx, _ry, red_visited, maze):
                    for blue_idx in range(4):
                        _bx, _by = bx + dx[blue_idx], by + dy[blue_idx]
                        if check(_bx, _by, blue_visited, maze) and (_rx, _ry) != (_bx, _by):
                            # 이동하려는 red좌표가 현재의 blue좌표이고, 이동하려는 blue좌표가 현재의 red좌표인 경우 X
                            if (_rx, _ry) == (bx, by) and (rx, ry) == (_bx, _by):
                                continue

                            rv = [v[:] for v in red_visited]
                            bv = [v[:] for v in blue_visited]
                            rv[_rx][_ry] = True
                            bv[_bx][_by] = True
                            queue.append((_rx, _ry, _bx, _by, rv, bv, cnt + 1))


    return 0 if answer == int(1e9) else answer


def check(x, y, visited, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 5 and not visited[x][y]

