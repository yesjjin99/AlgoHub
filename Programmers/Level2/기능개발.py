import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))])

    while queue:
        cnt = 1
        q = queue.popleft()
        while queue and q >= queue[0]:
            queue.popleft()
            cnt += 1
        answer.append(cnt)

    return answer

