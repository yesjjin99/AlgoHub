isused1 = [0]*40
isused2 = [0]*40
isused3 = [0]*40

def solve(level):
    global cnt, N
    if level == N:
        cnt += 1
        return
    for i in range(N):
        if isused1[i] or isused2[i+level] or isused3[level-i+N-1]: continue
        isused1[i] = True
        isused2[i + level] = True
        isused3[level - i + N - 1] = True
        solve(level + 1)
        isused1[i] = False
        isused2[i + level] = False
        isused3[level - i + N - 1] = False

N = int(input())
cnt = 0
solve(0)
print(cnt)
