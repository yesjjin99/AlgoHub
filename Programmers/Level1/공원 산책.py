def solution(park, routes):
    dx = {'N': -1, 'S': 1, 'W': 0, 'E': 0}
    dy = {'N': 0, 'S': 0, 'W': -1, 'E': 1}

    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j
                break

    for route in routes:
        op, n = route.split()
        tmp_x, tmp_y = x, y

        for _ in range(int(n)):
            nx, ny = x + dx[op], y + dy[op]

            # 주어진 방향으로 이동할 때 공원을 벗어나는 경우
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
                x, y = tmp_x, tmp_y
                break

            # 주어진 방향으로 이동 중 장애물을 만나는 경우
            if park[nx][ny] == 'X':
                x, y = tmp_x, tmp_y
                break

            x, y = nx, ny

    return [x, y]