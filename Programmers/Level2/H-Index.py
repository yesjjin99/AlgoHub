def solution(citations):
    citations.sort(reverse=True)
    res = [min(h, i + 1) for i, h in enumerate(citations)]
    return max(res)


def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
