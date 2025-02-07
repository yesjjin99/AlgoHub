import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]

medals.sort(key = lambda x: (-x[1], -x[2], -x[3]))  # 금 - 은 - 동의 수가 많은 순서대로 정렬

result = 1
for i in range(n):
    if i > 0 and medals[i - 1][1:] != medals[i][1:]:
        result = i + 1

    if medals[i][0] == k:
        break

print(result)