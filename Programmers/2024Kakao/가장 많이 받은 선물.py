from collections import defaultdict

def solution(friends, gifts):
    answer = []
    present = defaultdict(list)  # 선물을 준 기록
    count = {f: 0 for f in friends}  # 선물 지수

    for g in gifts:
        a, b = g.split()
        present[a].append(b)
        count[a] += 1
        count[b] -= 1

    for a in friends:
        result = 0
        for b in friends:
            if a == b:
                continue

            atob = present[a].count(b)
            btoa = present[b].count(a)

            if atob > btoa:
                result += 1
            if (atob == btoa or atob == btoa == 0) and count[a] > count[b]:
                result += 1

        answer.append(result)

    return max(answer)