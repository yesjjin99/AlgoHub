t = int(input())
inf = 10e18
for _ in range(t):
    dp = [inf]*100500
    dp[0] = 0
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(100000, -1, -1):
            if i >= a:
                dp[i] = min(dp[i] + b, dp[i-a])
            else: dp[i] += b
        c = inf
        for i in range(100001):
            c = min(c, max(dp[i], i))
    print(c)
    