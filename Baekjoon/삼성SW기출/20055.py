from collections import deque

n, k = map(int, input().split())
a = deque(list(map(int, input().split())))

def bfs():
    result = 0
    belt = deque([False] * n)

    while True:
        result += 1

        # 1. 벨트가 로봇과 함께 회전
        belt.rotate(1)
        a.rotate(1)

        if belt[n - 1]:
            belt[n - 1] = False  # 로봇이 내리는 위치에 도달하면, 즉시 내리기

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
        for i in range(n - 2, -1, -1):  # 벨트의 역순대로 진행하면 로봇이 벨트에 올라온 순서와 일치한다
            if belt[i] and not belt[i + 1] and a[i + 1] >= 1:  # 이동하려는 칸에 로봇이 없고, 그 칸의 내구도 1 이상 남아있어야 함
                belt[i], belt[i + 1] = False, True
                a[i + 1] -= 1

        if belt[n - 1]:
            belt[n - 1] = False  # 로봇이 내리는 위치에 도달하면, 즉시 내리기

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
        if a[0] > 0:
            belt[0] = True
            a[0] -= 1

        # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
        if a.count(0) >= k:
            break

    return result

print(bfs())
