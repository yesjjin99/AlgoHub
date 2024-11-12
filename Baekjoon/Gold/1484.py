N = int(input())
left = 0; right = 0
L = []; ans = []
for i in range(1, 200000):
    L.append(i*i)
while 1:
    if right >= len(L): break
    dif = L[right] - L[left]
    if dif < N: right += 1
    if dif > N: left += 1
    if dif == N:
        ans.append(int(L[right]**0.5))
        right += 1
if ans:
    for i in range(len(ans)):
        print(ans[i])
else: print(-1)
