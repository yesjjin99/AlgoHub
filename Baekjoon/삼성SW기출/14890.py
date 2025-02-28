n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check_row(i):  # 한 행 확인
    j = 0
    visited = [0] * n  # 경사면이 놓인 위치

    while True:
        if j == n - 1:  # 마지막 칸까지 성공적으로 이동한 경우
            return True

        if graph[i][j] == graph[i][j + 1]:  # 다음 칸의 높이가 같다면
            j += 1  # 다음 칸으로 이동
        elif graph[i][j] - graph[i][j + 1] == -1:  # 높이 차가 1이면서, 왼쪽의 높이가 더 작은 경우 -> 왼쪽으로 경사로 놓기
            if j - l + 1 < 0:
                return False
            for k in range(j - l + 1, j + 1):
                if graph[i][k] != graph[i][j] or visited[k]:  # 경사면을 놓을 칸의 높이가 모두 같지 않다면 or 이미 경사로를 놓은 곳이라면
                    return False
                visited[k] = 1  # 경사로 놓기

            j += 1  # 다음 칸으로 이동
        elif graph[i][j] - graph[i][j + 1] == 1:  # 높이 차가 1이면서, 오른쪽의 높이가 더 작은 경우 -> 오른쪽으로 경사로 놓기
            if j + l >= n:
                return False
            for k in range(j + 1, j + l + 1):
                if graph[i][k] != graph[i][j + 1] or visited[k]:
                    return False
                visited[k] = 1  # 경사로 놓기

            j += l  # 경사로가 놓인 마지막 위치로 이동
        else:  # 높이 차가 1이 아닌 경우
            return False


def check_column(j):  # 한 열 확인
    i = 0
    visited = [0] * n  # 경사면이 놓인 위치

    while True:
        if i == n - 1:  # 마지막 칸까지 성공적으로 이동한 경우
            return True

        if graph[i][j] == graph[i + 1][j]:  # 다음 칸의 높이가 같다면
            i += 1  # 다음 칸으로 이동
        elif graph[i][j] - graph[i + 1][j] == -1:  # 높이 차가 1이면서, 위쪽의 높이가 더 작은 경우 -> 위쪽으로 경사로 놓기
            if i - l + 1 < 0:
                return False
            for k in range(i - l + 1, i + 1):
                if graph[k][j] != graph[i][j] or visited[k]:  # 경사면을 놓을 칸의 높이가 모두 같지 않다면 or 이미 경사로를 놓은 곳이라면
                    return False
                visited[k] = 1  # 경사로 놓기

            i += 1  # 다음 칸으로 이동
        elif graph[i][j] - graph[i + 1][j] == 1:  # 높이 차가 1이면서, 아래쪽의 높이가 더 작은 경우 -> 아래쪽으로 경사로 놓기
            if i + l >= n:
                return False
            for k in range(i + 1, i + l + 1):
                if graph[k][j] != graph[i + 1][j] or visited[k]:
                    return False
                visited[k] = 1  # 경사로 놓기

            i += l  # 경사로가 놓인 마지막 위치로 이동
        else:  # 높이 차가 1이 아닌 경우
            return False

answer = 0
for x in range(n):
    if check_row(x):
        answer += 1
    if check_column(x):
        answer += 1

print(answer)