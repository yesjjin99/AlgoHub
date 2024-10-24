import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = []
    temp = list(map(int, input().split()))
    for i in range(0, n * m, m):
        dp.append(temp[i:i + m])

    for j in range(1, m):
        for i in range(n):
            if i == 0:  # 맨 윗 줄인 경우
                dp[i][j] += max(dp[i][j - 1], dp[i + 1][j - 1])
            elif i == n - 1:  # 맨 아래 줄인 경우
                dp[i][j] += max(dp[i - 1][j - 1], dp[i][j - 1])
            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

    result = 0
    for d in dp:
        result = max(result, max(d))
    print(result)
