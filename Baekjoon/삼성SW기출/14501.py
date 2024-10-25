n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [0] * (n + 1)
for i in range(n):
    for j in range(i + arr[i][0], n + 1):  # 마지막 날의 상담 기간이 1인 경우까지 포함
        dp[j] = max(dp[j], dp[i] + arr[i][1])

print(dp[-1])
