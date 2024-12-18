import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[deque() for _ in range(n)] for _ in range(n)]
fireball = deque()

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]  # 이동 방향

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireball.append((r - 1, c - 1, m, s, d))

for _ in range(k):
    while fireball:  # 모든 파이어볼 이동
        x, y, m, s, d = fireball.popleft()
        nx, ny = (x + dx[d] * s) % n, (y + dy[d] * s) % n  # 자신의 방향 d로 속력 s칸 만큼 이동 (1번 - n번 행 연결)
        graph[nx][ny].append((m, s, d))

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) == 1:
                m, s, d = graph[i][j].popleft()
                fireball.append((i, j, m, s, d))
            elif len(graph[i][j]) >= 2:  # 2개 이상의 파이어볼이 있는 칸
                nm, ns, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:  # 나누어진 파이어볼의 질량, 속력, 방향 계산
                    m, s, d = graph[i][j].popleft()
                    nm += m
                    ns += s
                    if d % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1

                nm //= 5
                ns //= cnt
                if cnt_even == cnt or cnt_odd == cnt:  # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수
                    dir = [0, 2, 4, 6]
                else:
                    dir = [1, 3, 5, 7]

                if nm == 0:  # 질량이 0인 파이어볼은 소멸
                    continue

                for nd in dir:
                    fireball.append((i, j, nm, ns, nd))

print(sum(f[2] for f in fireball))  # 남아있는 파이어볼 질량의 합
