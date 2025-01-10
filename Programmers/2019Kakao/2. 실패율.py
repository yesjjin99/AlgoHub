from collections import Counter

def solution(N, stages):
    answer, zero = [], []
    total = 0
    cnt = Counter(stages)

    for i in range(N + 1, 0, -1):
        if i == N + 1:
            total += cnt[i]
            continue

        if i in cnt:
            total += cnt[i]
            answer.append((cnt[i] / total, i))
        else:
            zero.append(i)


    zero.sort()
    answer.sort(key=lambda x: (-x[0], x[1]))

    return [x[1] for x in answer] + zero
