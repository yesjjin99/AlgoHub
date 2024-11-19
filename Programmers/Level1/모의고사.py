def solution(answers):
    math = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = [0] * 3

    for i in range(3):
        for j, a in enumerate(answers):
            if a == math[i][j % len(math[i])]:
                result[i] += 1

    return [i + 1 for i, r in enumerate(result) if r == max(result)]
