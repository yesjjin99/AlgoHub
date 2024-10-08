def solution(s):
    answer = []
    if len(s) == 1:
        return 1

    for c in range(1, len(s) // 2 + 1):
        cnt = 1
        tmp = ''
        for i in range(0, len(s), c):
            if s[i:i + c] == s[i + c:i + 2 * c]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += s[i:i + c]
                else:
                    tmp += str(cnt) + s[i:i + c]
                cnt = 1
        answer.append(len(tmp))

    return min(answer)
