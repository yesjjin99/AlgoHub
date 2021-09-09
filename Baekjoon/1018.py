mat = []
N, M = map(int, input().split())
for i in range(N):
    mat.append(input())

ans = 1e9
for a in range(N-7):
    for b in range(M-7):
        num1 = 0; num2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if mat[i][j] == 'W':
                    if (i+j) % 2 == 0: num1 += 1
                    else: num2 += 1
                else:
                    if (i+j) % 2 == 0: num2 += 1
                    else: num1 += 1
        ans = min(ans, num1, num2)
print(ans)
