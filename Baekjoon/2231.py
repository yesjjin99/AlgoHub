N = int(input())
for i in range(1, N):
    S = i
    temp = i
    while temp:
        S += temp % 10
        temp //= 10
    if N == S:
        print(i)
        exit()
print(0)
