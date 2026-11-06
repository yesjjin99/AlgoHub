def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]  # 현재까지 i행 j열을 밟았을 때의 최고점

    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, len(land)):
        # 바로 이전 행을 가장 점수가 높은 순대로 나열
        tmp = sorted([(i, v) for i, v in enumerate(dp[i - 1])], key=lambda x: x[1], reverse=True)

        for j in range(4):
            if j == tmp[0][0]:  # 현재 행의 j칸과 이전 행의 j칸이 모두 최대값일 경우, 이전 행에서는 두번째로 최대값을 선택해야 함 (연속으로 같은 열 밟을 수 없음)
                dp[i][j] = dp[i - 1][tmp[1][0]] + land[i][j]
            else:
                dp[i][j] = dp[i - 1][tmp[0][0]] + land[i][j]

    return max(dp[-1])