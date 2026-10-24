from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    count = len(q1) + len(q2) + 2  # 최대 이동 횟수

    if (s1 + s2) % 2 == 1:
        return -1

    # 총합이 더 큰 큐의 원소 pop - 총합이 더 작은 큐에 해당 원소 append
    while s1 != s2:  # 두 큐의 합이 같아질 때까지 반복
        if count > 0:
            if s1 > s2:
                i = q1.popleft()
                q2.append(i)
                s1 -= i
                s2 += i
            elif s1 < s2:
                i = q2.popleft()
                q1.append(i)
                s1 += i
                s2 -= i

            count -= 1
            answer += 1

        else:  # # 최대 이동 횟수 초과시 -1 리턴
            return -1

    return answer