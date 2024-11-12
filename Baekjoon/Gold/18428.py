dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
answer = False

def backtracking(cnt):  # 백트래킹을 통해 장애물 3개를 설치한 모든 경우 감시
    global answer
    if cnt == 3:
        if bfs():
            answer = True
            return
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    backtracking(cnt + 1)
                    graph[i][j] = 'X'

def bfs():
    for t in teacher:
        for i in range(4):
            nx, ny = t
            while 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 'O':  # 장애물
                    break
                if graph[nx][ny] == 'S':  # 학생
                    return False

                nx += dx[i]
                ny += dy[i]
    return True


n = int(input())
graph = []
teacher = []
for i in range(n):
    tmp = input().split()
    graph.append(tmp)
    for j, v in enumerate(tmp):
        if v == 'T':
            teacher.append((i, j))  # 선생님 위치

backtracking(0)

print("YES" if answer else "NO")
