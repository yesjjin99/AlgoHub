import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city, house, chicken = [], [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    city.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 1:
            house.append((i, j))
        elif tmp[j] == 2:
            chicken.append((i, j))

def distance(chicken):
    total = 0
    for i, j in house:
        tmp = []
        for x, y in chicken:
            tmp.append(abs(i - x) + abs(j - y))
        total += min(tmp)
    return total

answer = []
candidates = list(combinations(chicken, m))  # 백트래킹을 사용할 경우, 이미 지난 인덱스는 다시 방문하지 않도록 해야 함 -> 안 그러면 시간 초과 뜸!
for candidate in candidates:
    answer.append(distance(candidate))
print(min(answer))
