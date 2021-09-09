import sys
input = sys.stdin.readline
N, M = map(int, input().split())
line = []
for i in range(N):
    line.append(int(input()))

high = 10**18
low = 1
answer = high
while high >= low:
    mid = (high + low)//2
    S = 0
    for i in range(N):
        S += mid//line[i]
        if S >= M: break
    if S >= M:
        if mid < answer:
            answer = mid
        high = mid - 1
    else:
        low = mid + 1
print(answer)
