from collections import deque

def check(b, t):
    cnt = 0
    for i in range(len(b)):
        if b[:i] + b[i+1:] == t[:i] + t[i+1:]:
            cnt += 1
    return cnt == 1

def solution(begin, target, words):
    visited = [0] * (len(words) + 1)
    queue = deque([(begin, 0)])

    target_idx = ''
    for i, v in enumerate(words):
        if v == target:
            target_idx = i
    if target_idx == '':
        return 0

    while queue:
        v, i = queue.popleft()
        for j, w in enumerate(words):
            if check(v, w) and not visited[j]:
                queue.append((w, j))
                visited[j] = visited[i] + 1

    return visited[target_idx]
