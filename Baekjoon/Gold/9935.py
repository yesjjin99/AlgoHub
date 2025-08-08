import sys
sys.setrecursionlimit(10 ** 6)

s = input()
target = input()
t_len = len(target)

result = []
for c in s:
    result.append(c)
    if c == target[-1] and ''.join(result[-t_len:]) == target:
        for _ in range(t_len):
            result.pop()

print(''.join(result) if result else 'FRULA')