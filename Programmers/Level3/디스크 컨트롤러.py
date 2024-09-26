import heapq as hq

def solution(jobs):
    result, time = 0, 0
    num = len(jobs)
    ready = []  # 요청 들어온 작업들 목록
    hq.heapify(jobs)  # 작업 목록

    while jobs or ready:
        # 현재 시점에서 수행 가능한 작업들 -> 소요시간 기준으로 최소힙 구성
        while jobs:
            if jobs[0][0] > time:
                break
            job = hq.heappop(jobs)
            hq.heappush(ready, (job[1], job[0]))

        # 현재 시점에서 수행 가능한 작업들 중 가장 소요시간이 적은 작업 수행
        if ready:
            j = hq.heappop(ready)
            time += j[0]
            result += time - j[1]
        else:
            time += 1

    return result // num
