s = input()
alpha, num = '', 0
for c in s:
    if c.isdigit():
        num += int(c)
    else:
        alpha += c

if num != 0:
    print("".join(sorted(alpha)) + str(num))
else:
    print("".join(sorted(alpha)))
