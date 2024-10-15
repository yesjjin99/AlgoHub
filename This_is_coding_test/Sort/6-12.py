n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(k):
    a.sort()
    b.sort(reverse=True)

    if a[0] < b[0]:
        a[0], b[0] = b[0], a[0]
    else:
        break

print(sum(a))