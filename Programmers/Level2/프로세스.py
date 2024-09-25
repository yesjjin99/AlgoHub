from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque((i, v) for i, v in enumerate(priorities))

    while q:
        i, v = q.popleft()
        if any(v < p[1] for p in q):
            q.append((i, v))
        else:
            answer += 1
            if i == location:
                return answer


from collections import deque


# max 값 업데이트해주는 방식 -> 시간복잡도 더 빠름
def solution(priorities, location):
    answer = 0
    q = deque((i, v) for i, v in enumerate(priorities))
    m = max(priorities)

    while q:
        i, v = q.popleft()
        if v < m:
            q.append((i, v))
        else:
            answer += 1
            if i == location:
                return answer
            priorities[i] = 0
            m = max(priorities)
