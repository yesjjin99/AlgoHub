n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, / 순
result = []

def dfs(i, total, op):
    if i == n:
        result.append(total)
        return

    if op[0] != 0:
        op[0] -= 1
        dfs(i + 1, total + nums[i], op)
        op[0] += 1  # 백트래킹 : 연산자를 바꿔가며 모든 경우를 계산해야 하므로 이전 상태로 되돌려야 한다
    if op[1] != 0:
        op[1] -= 1
        dfs(i + 1, total - nums[i], op)
        op[1] += 1
    if op[2] != 0:
        op[2] -= 1
        dfs(i + 1, total * nums[i], op)
        op[2] += 1
    if op[3] != 0:
        op[3] -= 1
        if total >= 0:
            dfs(i + 1, total // nums[i], op)
        else:
            dfs(i + 1, -(-total // nums[i]), op)
        op[3] += 1


dfs(1, nums[0], op)
print(max(result))
print(min(result))
