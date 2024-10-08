n = list(map(int, input()))
idx = len(n) // 2
if sum(n[:idx]) == sum(n[idx:]):
    print("LUCKY")
else:
    print("READY")
