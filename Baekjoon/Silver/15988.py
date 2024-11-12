import sys
dp = [0]*1000010
MOD = 1000000009
input = sys.stdin.readline
#많은 입력을 받을 때 속도 향상
dp[1] = 1; dp[2] = 2; dp[3] = 4
for i in range(4, 1000001):
    dp[i] += dp[i-1] + dp[i-2] + dp[i-3]
    dp[i] %= MOD

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
    