def solution(name):
    answer = 0
    move = len(name) - 1

    for i, v in enumerate(name):
        answer += min(ord(v) - ord('A'), ord('Z') - ord(v) + 1)  # 위 아래 조작 횟수

        next = i + 1  # 연속된 A들 중 가장 마지막 인덱스 (ex. BBBBAAAAB)
        while next < len(name) and name[next] == 'A':
            next += 1

        # 1. 오른쪽으로 이동하여 연속하는 A의 왼쪽까지 갔다가 -> 왼쪽으로 이동하여 연속하는 A의 오른쪽까지 이동
        # 2. 왼쪽으로 연속하는 A의 오른쪽까지 갔다가 -> 다시 오른쪽으로 이동하여 연속하는 A의 왼쪽까지 이동
        # 각 인덱스의 위치를 기준으로 한 왼-오 조작 횟수 중 가장 작은 값이 최적의 이동 경로
        move = min(move, 2 * i + len(name) - next, 2 * (len(name) - next) + i)

    answer += move
    return answer
