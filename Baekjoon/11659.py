import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pre = list(map(int, input().split()))
for i in range(N-1):
    pre[i+1] += pre[i]
pre = [0] + pre
for i in range(M):
    a, b = map(int, input().split())
    print(pre[b] - pre[a-1])
    