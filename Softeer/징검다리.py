import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:  # 더 높은 돌인 경우
            dp[i] = max(dp[i], dp[j] + 1)  # 현재 값과 j번째 돌에서 넘어올 때의 개수 비교

print(max(dp))