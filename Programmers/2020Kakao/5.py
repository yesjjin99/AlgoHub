# 기둥과 보 설치
def check(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            # 바닥 위 or 왼쪽에 있는 보의 위 or 오른쪽에 있는 보의 위 or 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        else:
            # 왼쪽 끝이 기둥 위 or 오른쪽 끝이 기둥 위 or 양쪽 끝이 다른 보와 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                 continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if x < 0 or x > n or y < 0 or y > n:
            continue
        if b == 1:  # 설치
            answer.append([x, y, a])  # 일단 설치 후
            if not check(answer):
                answer.remove([x, y, a])  # 조건을 만족하지 않으면 제거
        else:  # 삭제
            answer.remove([x, y, a])  # 일단 제거 후
            if not check(answer):
                answer.append([x, y, a])  # 조건을 만족하지 않으면 다시 설치

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))
