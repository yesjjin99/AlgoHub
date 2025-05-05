n = int(input())
board = [[]]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

def count(x, y, d1, d2):  # 기준점 (x, y)와 경계의 길이 d1, d2일 때 -> 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이
    total = [0] * 5  # 각 선거구의 인구 수
    divide = [[0] * (n + 1) for _ in range(n + 1)]  # 선거구

    # 경계선
    for i in range(d1 + 1):
        divide[x + i][y - i] = 1  # 왼쪽, 위로 향하는 대각선
        divide[x + d2 + i][y + d2 - i] = 1  # 오른쪽, 위로 향하는 대각선
    for j in range(d2 + 1):
        divide[x + j][y + j] = 1  # 오른쪽, 아래로 향하는 대각선
        divide[x + d1 + j][y - d1 + j] = 1  # 왼쪽, 아래로 향하는 대각선

    # 5번 선거구 채우기
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(n + 1):
            if divide[i][j] == 1:  # 경계구역 다시 만날 때까지
                flag = not flag
            else:
                if flag:
                    divide[i][j] = 1

    # 나눈 구역으로 인구 수 카운트하기
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < x + d1 and j <= y and divide[i][j] != 1:
                total[0] += board[i][j]
            elif i <= x + d2 and y < j and divide[i][j] != 1:
                total[1] += board[i][j]
            elif x + d1 <= i and j < y - d1 + d2 and divide[i][j] != 1:
                total[2] += board[i][j]
            elif x + d2 < i and y - d1 + d2 <= j and divide[i][j] != 1:
                total[3] += board[i][j]
            elif divide[i][j] == 1:
                total[4] += board[i][j]

    return max(total) - min(total)

answer = int(1e9)
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    answer = min(answer, count(x, y, d1, d2))
print(answer)