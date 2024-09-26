import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    while len(scoville) >= 2 and scoville[0] < K:
        s1 = hq.heappop(scoville)
        s2 = hq.heappop(scoville)
        hq.heappush(scoville, s1 + s2 * 2)
        answer += 1

    return answer if scoville[0] >= K else -1
