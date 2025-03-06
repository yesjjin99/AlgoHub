import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = b + 1  # a번 점선 위치에서 b번 세로선 - b+1번 세로선 연결
    graph[a][b + 1] = b

def check(graph):
    result = 0
    for a in range(1, n + 1):  # 1번 세로선 ~ n번 세로선 모두 체크
        i, j = 1, a
        while i <= h:
            if graph[i][j] != 0:
                j = graph[i][j]  # 옆 칸으로 이동
            i += 1

        if j == a:  # j번 세로선의 결과가 j번이 나오는 경우
            result += 1
    return result == n  # 모든 세로선이 자기 자신의 번호로 결과가 나오는지 여부

def make_line(graph, count, x):
    global answer

    if answer <= count:  # 가로선을 정답보다 많이 만든 경우 확인할 필요 X
        return
    if check(graph):  # 모든 세로선이 자기 자신의 번호로 결과가 나온다면
        answer = min(answer, count)
        return
    if count == 3:  # 정답이 3보다 큰 값은 어차피 -1로 출력하므로 더 이상 확인할 필요 X
        return

    for i in range(x, h + 1):
        for j in range(1, n):
            if graph[i][j] == 0 and graph[i][j + 1] == 0:
                graph[i][j], graph[i][j + 1] = j + 1, j
                make_line(graph, count + 1, i)
                graph[i][j], graph[i][j + 1] = 0, 0


answer = 4
make_line(graph, 0, 1)
if answer > 3:  # 정답이 3보다 큰 값이면 -1을 출력
    answer = -1
print(answer)