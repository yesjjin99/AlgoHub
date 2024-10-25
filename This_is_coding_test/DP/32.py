n = int(input())
dp = [[0] * n for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        dp[i][j] = tmp[j]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[-1]))
