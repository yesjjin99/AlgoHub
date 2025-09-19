import sys
sys.setrecursionlimit(10 ** 6)

board_red = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12,
             12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 21: 22, 22: 23,
             23: 24, 25: 26, 26: 24, 27: 28, 28: 29, 29: 24, 24: 30, 30: 31, 31: 20, 20: 32, 32: 32}
board_blue = {5: 21, 10: 25, 15: 27}
scores = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22, 12: 24,
          13: 26, 14: 28, 15: 30, 16: 32, 17: 34, 18: 36, 19: 38, 20: 40, 21: 13, 22: 16, 23: 19,
          24: 25, 25: 22, 26: 24, 27: 28, 28: 27, 29: 26, 30: 30, 31: 35, 32: 0}

answer = 0
dice = list(map(int, input().split()))

# 1. 파란색에서 이동 시작 -> blue로 이동
# 2. 그 외에는 -> red로 이동
# 3. 도착 칸(40)에 도착하면 무조건 종료 => 도착 칸에 도착하면 해당 말은 제거 (-1)
# 이동을 마치는 칸에 다른 말이 있으면 그 말은 불가능
# 이동할 때마다 수가 점수에 추가

def backtracking(depth, result, horses):  # Greedy가 아닌 백트래킹으로 최댓값 해결 (그래프)
    global answer

    if depth == 10:
        answer = max(answer, result)
        return

    for i in range(4):
        x = horses[i]  # 현재 말의 위치

        if x in board_blue:  # 현재 칸이 파란색이라면 1) blue 선으로 이동 2) c - 1 만큼 빨간색으로 이동
            x = board_blue[x]
        else:  # 그 외에는 모두 c만큼 빨간색으로 이동
            x = board_red[x]

        for _ in range(dice[depth] - 1):
            if x == 32:
                break
            x = board_red[x]

        if x == 32 or (x < 32 and x not in horses):  # 도착 칸에 도착했거나 or 이동칸에 말이 없는 경우
            before = horses[i]  # 이전 말의 위치

            horses[i] = x  # 현재 말 위치 갱신
            backtracking(depth + 1, result + scores[x], horses)
            horses[i] = before


backtracking(0, 0, [0, 0, 0, 0])  # 시작 칸에 말 4개
print(answer)