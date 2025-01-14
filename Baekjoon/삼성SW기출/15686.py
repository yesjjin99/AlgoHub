n, m = map(int, input().split())
houses, chickens = [], []
for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n):
        if city[j] == 1:  # 집
            houses.append((i, j))
        elif city[j] == 2:  # 치킨집
            chickens.append((i, j))

visited = [0] * len(chickens)
result = 1e9

def dfs(idx, count):
    global result

    if count == m:  # 도시에 있는 치킨집 중에서 M개 선택
        total = 0  # 도시의 치킨 거리
        for hx, hy in houses:
            tmp = 1e9
            for i, (cx, cy) in enumerate(chickens):
                if visited[i]:
                    tmp = min(tmp, abs(cx - hx) + abs(cy - hy))  # 각 집의 치킨 거리 계산
            total += tmp

        result = min(result, total)
        return

    for i in range(idx, len(chickens)):  # 백트래킹을 사용할 경우, 이미 지난 인덱스는 다시 방문하지 않도록 해야 함 -> 안 그러면 시간 초과 뜸!
        if not visited[i]:
            visited[i] = 1  # 치킨집 선택
            dfs(i + 1, count + 1)
            visited[i] = 0

dfs(0, 0)
print(result)

# ---

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