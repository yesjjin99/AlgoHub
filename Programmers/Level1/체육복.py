def solution(n, lost, reserve):
    lo = list(set(lost) - set(reserve))
    re = list(set(reserve) - set(lost))
    answer = n - len(lo)

    for l in lo:
        for r in re:
            if l - 1 == r or l + 1 == r:
                answer += 1
                re.remove(r)

    return answer
