import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pre = [[0]*(N+1)]
for i in range(N):
    pre.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        pre[i][j] += pre[i][j-1] + pre[i-1][j] - pre[i-1][j-1]

for i in range(M):
    a, b, c, d = map(int, input().split())
    print(pre[c][d] - pre[a-1][d] - pre[c][b-1] + pre[a-1][b-1])
    