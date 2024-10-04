s = input()
cnt0, cnt1 = 0, 0

if s[0] == '0':
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '0':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))