answer = -1

def solution(N, number):

    def dfs(cnt, result):
        global answer

        if cnt > 8:
            return
        if result == number:
            if cnt < answer or answer == -1:
                answer = cnt
            return

        n = 0
        for i in range(8):
            n = n * 10 + N
            dfs(cnt + i + 1, result + n)  # N을 사용한 횟수
            dfs(cnt + i + 1, result - n)
            dfs(cnt + i + 1, result * n)
            dfs(cnt + i + 1, result // n)

    dfs(0, 0)
    return answer

# ---

def solution(N, number):
    dp = [{}]

    x = 0
    for i in range(1, 9):  # N 사용횟수가 i번일 때, 나올 수 있는 값들
        dp.append(set())
        x = x * 10 + N
        dp[i].add(x)  # N, NN, NNN ...

        for j in range(i):
            for op1 in dp[j]:  # N을 j번 사용해서 만들 수 있는 값들 (+, -, *, //) N을 (i-j)번 사용해서 만들 수 있는 값들 = N을 총 i번 사용해서 나올 수 있는 값들
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        if number in dp[i]:
            return i

    return -1
