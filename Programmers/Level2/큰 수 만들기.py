def solution(number, k):
    result = []
    for n in number:
        while result and result[-1] < n and k > 0:
            result.pop()
            k -= 1
        result.append(n)

    if k > 0:
        result = result[:-k]
    return "".join(result)
