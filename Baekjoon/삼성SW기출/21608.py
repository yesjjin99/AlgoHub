n = int(input())
students = [list(map(int, input().split())) for _ in range(n * n)]
graph = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for student in students:
    pos = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0:  # 비어있는 칸이어야 함
                continue

            like, blank = 0, 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] in student[1:]:  # 좋아하는 학생이 인접한 칸
                        like += 1
                    if graph[nx][ny] == 0:  # 인접한 칸 중에서 비어있는 칸
                        blank += 1
            pos.append([-like, -blank, x, y])  # like, blank는 큰 순서대로 / x, y는 작은 순서대로 정렬해야 함

    pos.sort()
    graph[pos[0][2]][pos[0][3]] = student[0]

result = 0
for x in range(n):
    for y in range(n):
        likes = []
        for student in students:
            if student[0] == graph[x][y]:
                likes = student[1:]
                break

        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] in likes:
                cnt += 1

        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)