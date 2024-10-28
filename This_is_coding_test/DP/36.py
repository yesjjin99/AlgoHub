def edit_dist(str1, str2):
    n, m = len(str1), len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):  # DP 테이블 초기 설정
        dp[i][0] = i
    for i in range(1, m + 1):
        dp[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:  # 문자가 같다면, 왼쪽 위에 해당하는 수 그대로 대입
                dp[i][j] = dp[i - 1][j - 1]
            else:  # 문자가 다르다면 -> 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중 최소 비용 대입
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

    return dp[n][m]

str1 = input()
str2 = input()

edit_dist(str1, str2)
