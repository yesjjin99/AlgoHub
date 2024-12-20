n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def check(line):
    visited = [False] * n  # 경사로가 생기는 곳 체크
    for i in range(0, n - 1):
        if line[i] == line[i + 1]:  # 바로 다음 위치의 높이와 같으면 통과
            continue
        elif abs(line[i] - line[i + 1]) > 1:  # 다음 위치와의 높이 차가 1 이상이면 False
            return False
        elif line[i] > line[i + 1]:  # 현재 높이가 다음 높이보다 높은 경우
            for j in range(i + 1, i + l + 1):
                if j < 0 or j >= n:  # 경사의 길이가 범위 밖이면
                    return False
                if line[i + 1] != line[j]:  # 경사를 놓을 위치의 높이가 다르면
                    return False
                elif visited[j]:  # 높이는 모두 같지만 이미 경사로가 놓인 곳이면
                    return False

                visited[j] = True  # 경사로 놓기
        else:  # 현재 높이가 다음 높이보다 낮은 경우
            for j in range(i, i - l, -1):
                if j < 0 or j >= n:
                    return False
                if line[i] != line[j]:
                    return False
                elif visited[j]:
                    return False

                visited[j] = True

    return True

answer = 0
for b in board:  # 가로 길 체크
    if check(b):
        answer += 1
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(board[j][i])

    if check(tmp):
        answer += 1

print(answer)
