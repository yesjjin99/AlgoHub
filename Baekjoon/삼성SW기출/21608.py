n = int(input())
students = [list(map(int, input().split())) for _ in range(n ** 2)]
result = [[0] * n for _ in range(n)]  # 학생의 자리
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for student in students:
    # 모든 위치 탐색하며 가장 적합한 장소 찾기
    pos = []
    for x in range(n):
        for y in range(n):
            if result[x][y] != 0:  # 이미 자리에 학생이 앉아있는 경우
                continue

            likes, empty = 0, 0  # 이 자리에 앉는 경우 인접한 칸에 좋아하는 학생의 수, 빈 칸의 수
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if result[nx][ny] in student[1:]:  # 좋아하는 학생
                    likes += 1
                elif result[nx][ny] == 0:  # 빈 칸
                    empty += 1
            pos.append((x, y, likes, empty))

    pos.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))  # 좋아하는 학생이 많은 순 - 빈 칸이 많은 순 - 행의 번호 작은 순 - 열의 번호 작은 순으로 정렬
    result[pos[0][0]][pos[0][1]] = student[0]  # 자리 잡기

answer = 0  # 만족도
for x in range(n):
    for y in range(n):
        likes = []
        for student in students:
            if result[x][y] == student[0]:
                likes = student[1:]  # 자리에 있는 학생의 좋아하는 학생 구하기
                break

        count = 0  # 인접한 칸에 앉은 좋아하는 학생의 수
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and result[nx][ny] in likes:
                count += 1

        if count > 0:
            answer += 10 ** (count - 1)  # 만족도 계산

print(answer)