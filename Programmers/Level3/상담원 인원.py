from itertools import combinations_with_replacement, permutations
import heapq

def solution(k, n, reqs):

    def cal_wait_time(waitings, n):  # 유형 별 waiting_list에 n명의 상담 원이 있을 때 대기 시간 계산
        total = 0
        queue = []

        for _ in range(n):
            heapq.heappush(queue, 0)

        for start, duration in waitings:
            time = heapq.heappop(queue)  # 자리가 생기는 시간
            if start > time:  # # 현재 상담 가능한 경우(배정 가능한 상담사가 있는 경우)
                heapq.heappush(queue, duration)
            else:
                wait_time = time - start
                total += wait_time
                heapq.heappush(queue, duration + wait_time)

        return total

    answer = int(1e9)
    waiting = [[] for _ in range(k + 1)]  # 대기 리스트 (상담 요청)

    for a, b, c in reqs:
        waiting[c].append([a, a + b])  # c번 상담유형에 누가, 언제 들어와서 언제 끝나는지

    cases = set()
    for c in combinations_with_replacement(range(1, n - k + 1 + 1), k):
        if sum(c) == n:
            # 이 숫자 조합을 상담 유형 별로 배치하도록 변환
            case = set(permutations(c, k))
            cases = cases | case

    for case in cases:
        wait_time = 0
        for i in range(1, k + 1):  # i번 상담유형에 case[i] 만큼의 상담원이 들어갔을 때 대기시간
            wait_time += cal_wait_time(waiting[i], case[i - 1])
        answer = min(answer, wait_time)

    return answer