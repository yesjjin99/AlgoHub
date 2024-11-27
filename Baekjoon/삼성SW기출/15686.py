n, m = map(int,input().split())
home, chicken = [], []
for i in range(n): # 집과 치킨의 좌표를 리스트에 넣어준다.
    cities = list(map(int,input().split()))
    for j in range(n):
        if cities[j] == 1:
            home.append((i,j))
        elif cities[j] == 2:
            chicken.append((i,j))

visited = [False] * len(chicken)
result = 1e9

def dfs(idx,cnt):
    global result

    if cnt == m:
        total = 0
        for i, j in home: # 집 좌표에 대해 모든 치킨집과의 거리를 구함
            distance = 1e9 # 거리를 큰 수로 정의
            for x, (a, b) in enumerate(chicken):
                if visited[x]:
                    distance = min(distance, abs(i - a) + abs(j - b))  # 각 집의 치킨 거리(최소)
            total += distance
        result = min(total, result)  # 도시의 치킨 거리(최소)
        return

    for i in range(idx, len(chicken)):  # 백트래킹을 사용할 경우, 이미 지난 인덱스는 다시 방문하지 않도록 해야 함 -> 안 그러면 시간 초과 뜸!
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False

dfs(0,0)
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
