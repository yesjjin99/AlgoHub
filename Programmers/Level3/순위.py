def solution(n, results):
    answer = 0
    board = [[0] * n for _ in range(n)]

    for a, b in results:
        board[a - 1][b - 1] = 1
        board[b - 1][a - 1] = -1

    for k in range(n):  # 플로이드-워셜
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1, -1]:
                    continue

                if board[i][k] == board[k][j] == 1:  # i가 k를 이기고, k가 j를 이긴 경우
                    # i가 k와 j를 모두 이긴 것으로 간주
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1

    for row in board:
        if row.count(0) == 1:  # 순위가 결정되려면 모든 선수와 다 경기를 해봐야하므로 체크된 값의 개수가 n - 1 이면 된다
            answer += 1

    return answer