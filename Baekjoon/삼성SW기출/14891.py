from collections import deque

wheels = [deque(map(int, input().rstrip())) for _ in range(4)]

def rotate_left(n, d):
    if n == 0:
        return

    if wheels[n][6] != wheels[n - 1][2]:
        rotate_left(n - 1, -d)
        wheels[n - 1].rotate(-d)  # 톱니바퀴를 움직이기 전에, 인접한 톱니바퀴가 움직일 수 있는지 없는지를 검사한 뒤 회전


def rotate_right(n, d):
    if n == 3:
        return

    if wheels[n][2] != wheels[n + 1][6]:
        rotate_right(n + 1, -d)
        wheels[n + 1].rotate(-d)


for _ in range(int(input())):
    n, d = map(int, input().split())
    need_rotate = [(n - 1, d)]

    rotate_left(n - 1, d)  # 왼쪽으로 차례로 이동하며 확인
    rotate_right(n - 1, d)  # 오른쪽으로 차례로 이동하며 확인

    wheels[n - 1].rotate(d)

answer = 0
for i in range(4):
    if wheels[i][0] == 1:
        answer += 2 ** i
print(answer)
