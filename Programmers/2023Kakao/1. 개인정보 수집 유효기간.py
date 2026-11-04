def solution(today, terms, privacies):
    answer = []
    term = {}
    for t in terms:
        a, b = t.split()
        term[a] = int(b) * 28

    today = list(map(int, today.split('.')))
    for i in range(len(privacies)):
        total = 0
        date, type = privacies[i].split()
        date = list(map(int, date.split('.')))
        total += (today[0] - date[0]) * 12 * 28  # year
        total += (today[1] - date[1]) * 28  # month
        total += (today[2] - date[2])  # day

        if term[type] <= total:  # 오늘까지의 보관기간이 유효기간 이상이라면
            answer.append(i + 1)

    return answer
