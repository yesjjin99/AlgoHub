import sys
input = sys.stdin.readline

n, k = map(int, input().split())
diff = []
for _ in range(n):
    a, b = map(int, input().split())
    diff.append(b - a)

diff.sort()

if diff[k - 1] < 0:
    print(0)
else:
    print(diff[k - 1])