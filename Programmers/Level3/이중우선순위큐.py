import heapq as hq

def solution(operations):
    minq, maxq = [], []
    for op in operations:
        type, data = op.split()
        if type == "I":
            hq.heappush(minq, int(data))
            hq.heappush(maxq, -int(data))
        else:
            if not minq:
                continue
            if data == "-1":  # 최솟값 삭제
                m = hq.heappop(minq)
                maxq.remove(-m)
            else:
                m = hq.heappop(maxq)
                minq.remove(-m)

    if minq:
        return [-hq.heappop(maxq), hq.heappop(minq)]
    else:
        return [0, 0]
