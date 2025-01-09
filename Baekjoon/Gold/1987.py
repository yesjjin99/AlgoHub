r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

visited = set()  # 지금까지 지나온 모든 칸에 적혀 있는 알파벳
result = 0

def dfs(x, y, cnt):
    global result

    result = max(result, cnt)  # 최대 칸 수 갱신

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            visited.remove(board[nx][ny])

visited.add(board[0][0])
dfs(0, 0, 1)
print(result)