import math
import sys
input = sys.stdin.readline

answer = 0

n = int(input())
cnt = list(map(int, input().split()))
b, c = map(int, input().split())

answer += n  # 총감독관 각 시험장마다 1명씩 추가
for i in range(n):
    cnt[i] -= b
    if cnt[i] > 0:
        answer += math.ceil(cnt[i] / c)  # 부감독관 추가

print(answer)
