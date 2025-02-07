from collections import deque

n, s = map(int, input().split())
x = list(map(int, input().split()))
h = list(map(int, input().split()))
loc = list(enumerate(zip(x, h)))

s_loc = loc[s - 1]
loc.sort(key = lambda x: x[1][0])  # 위치 오름차순으로 정렬

def bfs(s_loc):
    queue = deque([s_loc])  # 자동차 번호, loc 에서 해당 자동차의 index
    visited = [0] * n
    visited[s - 1] = 1

    while queue:
        idx, [cx, ch] = queue.popleft()  # 움직일 자동차, 위치, 연료
        for i in range(idx - 1, -1, -1):  # 왼쪽으로 이동
            if loc[i][1][0] < cx - ch:  # 현재 자동차의 연료량으로 이동할 수 없는 위치에 있는 자동차라면
                break
            if visited[loc[i][0]]:
                continue

            queue.append(loc[i])
            visited[loc[i][0]] = 1
        for i in range(idx + 1, n):  # 오른쪽으로 이동
            if loc[i][1][0] > cx + ch:  # 현재 자동차의 연료량으로 이동할 수 없는 위치에 있는 자동차라면
                break
            if visited[loc[i][0]]:
                continue

            queue.append(loc[i])
            visited[loc[i][0]] = 1

    return visited

visited = bfs(s_loc)
for i in range(n):
    if visited[i]:
        print(i + 1, end=" ")