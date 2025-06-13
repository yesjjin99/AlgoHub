from collections import deque


def solution(game_board, table):
    answer = -1
    n = len(game_board)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    def bfs(graph, f):
        result = []
        visited = [[False] * len(graph[0]) for _ in range(len(graph))]

        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if not visited[i][j] and graph[i][j] == f:
                    queue = deque([(i, j)])
                    graph[i][j] = f ^ 1
                    visited[i][j] = True
                    lst = [(i, j)]

                    while queue:
                        x, y = queue.popleft()

                        for d in range(4):
                            nx, ny = x + dx[d], y + dy[d]
                            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == f:
                                queue.append((nx, ny))
                                graph[nx][ny] = f ^ 1
                                visited[nx][ny] = True
                                lst.append((nx, ny))

                    result.append(lst)

        return result

    def make_table(graph):  # 2차원 리스트의 형태로 만들기
        x_list, y_list = zip(*graph)
        a, b = max(x_list) - min(x_list) + 1, max(y_list) - min(y_list) + 1
        table = [[0] * b for _ in range(a)]

        for x, y in graph:
            table[x - min(x_list)][y - min(y_list)] = 1

        return table, len(graph)

    def rotate(graph):  # 90도 회전
        return list(map(list, zip(*graph[::-1])))


    empty = bfs(game_board, 0)  # game_board의 빈 공간 찾기
    puzzle = bfs(table, 1)  # table의 퍼즐 조각 찾기

    # game_board의 빈 공간에 맞는 퍼즐 조각 탐색
    for empty_origin in empty:
        filled = False
        e, ecnt = make_table(empty_origin)

        for puzzle_origin in puzzle:
            if filled:
                break

            p, pcnt = make_table(puzzle_origin)
            if ecnt != pcnt:
                continue

            for _ in range(4):
                p = rotate(p)
                if e == p:
                    answer += ecnt
                    puzzle.remove(puzzle_origin)
                    filled = True
                    break

    return answer