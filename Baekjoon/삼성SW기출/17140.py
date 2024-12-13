from collections import Counter

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
count = 0


def r_operation(arr):
    result, tmp = [], []
    max_len = 0
    for i, a in enumerate(arr):
        while 0 in a:
            a.remove(0)

        c = sorted(Counter(sorted(a)).items(), key=lambda x: (x[1], x[0]))
        tmp.append(list(sum(c, ())))
        max_len = max(max_len, len(tmp[i]))

    for t in tmp:
        if len(t) > 100:
            result.append(t[:100])
        else:
            result.append(t + [0] * (max_len - len(t)))

    return result, max_len

def c_operation(arr):
    lst = []
    for j in range(len(arr[0])):
        t = []
        for i in range(len(arr)):
            t.append(arr[i][j])
        lst.append(t)

    tmp, max_len = r_operation(lst)
    if max_len > 100:
        max_len = 100

    result = [[0] * len(arr[0]) for _ in range(max_len)]
    for j, t in enumerate(tmp):
        for i in range(len(t)):
            result[i][j] = t[i]

    return result


count = 0
while True:
    if len(arr) >= r and len(arr[0]) >= c and arr[r - 1][c - 1] == k:
        print(count)
        break
    if count > 100:
        print(-1)
        break

    count += 1
    if len(arr) >= len(arr[0]):
        arr, _ = r_operation(arr)
    else:
        arr = c_operation(arr)
