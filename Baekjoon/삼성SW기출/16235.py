from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # 매년 겨울 각 칸에 추가되는 양분의 양
ground = [[5] * n for _ in range(n)]  # 가장 처음에 양분은 모든 칸에 5만큼
tree = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
def add_tree(x, y):  # 나무 번식
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            tree[nx][ny].appendleft(1)  # 인접한 8개의 칸에 나이가 1인 나무 생성

def spring_summer():
    for i in range(n):
        for j in range(n):
            dead_tree = []  # 죽는 나무들
            tree_cnt = len(tree[i][j])
            for t in range(tree_cnt):
                if ground[i][j] >= tree[i][j][t]:
                    ground[i][j] -= tree[i][j][t]  # 자신의 나이만큼 양분을 먹기
                    tree[i][j][t] += 1  # 나이 1 증가
                else:  # 땅에 양분이 부족하다면
                    for _ in range(t, tree_cnt):  # 뒤의 나무들까지 모두 죽는다
                        dead_tree.append(tree[i][j].pop())
                    break

            while dead_tree:
                ground[i][j] += dead_tree.pop() // 2  # 죽은 나무가 양분으로 변하게 된다

def fall_winter():
    for i in range(n):
        for j in range(n):
            for t in range(len(tree[i][j])):
                if tree[i][j][t] % 5 == 0:  # 나이가 5의 배수일 경우, 나무 번식
                    add_tree(i, j)

            ground[i][j] += arr[i][j]  # 땅에 양분 추가

for _ in range(k):  # K년 반복
    spring_summer()
    fall_winter()

result = 0
for i in range(n):
    for j in range(n):
        result += len(tree[i][j])
print(result)