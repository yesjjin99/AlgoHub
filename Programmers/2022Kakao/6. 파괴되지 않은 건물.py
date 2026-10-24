def solution(board, skill):
    answer = 0

    # 미리 skill을 전부 합해서 최종 데미지를 구해놓기 (누적합)
    damage = [[0] * len(board[0] + 1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if type == 1: damage[i][j] -= degree
                elif type == 2: damage[i][j] += degree

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += damage[i][j]
            if board[i][j] > 0: answer += 1

    return answer