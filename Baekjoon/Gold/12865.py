import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]  # 무게, 가치

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):  # 물품
    for j in range(1, k + 1):  # 무게
        w, v = items[i]
        if j >= w:  # 현재 배낭의 허용 무게가 넣을 아이템의 무게보다 크거나 같은 경우 (즉, 현재 허용 무게에서 해당 아이템을 넣을 수 있는 경우)
            # 이전 배낭 그대로 vs 현재 넣을 무게만큼 배낭에서 빼고 + 현재 물건 넣기
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])