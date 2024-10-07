# 문자열 압축
def solution(s):
    result = []
    if len(s) == 1:
        return 1

    for j in range(1, len(s) // 2 + 1):
        cnt = 1
        tmp = ''
        for i in range(0, len(s), j):
            if s[i:i + j] == s[i + j:i + 2 * j]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += s[i:i + j]
                else:
                    tmp += str(cnt) + s[i:i + j]
                cnt = 1  # 초기화
        result.append(len(tmp))
    return min(result)

# ---

def compress(s, tok_len):
    words = [s[i:i + tok_len] for i in range(0, len(s), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1

    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1

    return sum(len(word) + len(str(cnt)) if cnt > 1 else 0 for word, cnt in res

def solution(s):
    return min(compress(s, tok_len) for tok_len in list(range(1, len(s) // 2 + 1)) + [len(s)])
