from itertools import product

def solution(users, emoticons):
    answer = []
    sales = list(product([0.4, 0.3, 0.2, 0.1], repeat = len(emoticons)))

    for sale in sales:
        cnt, total = 0, 0

        for a, b in users:  # 비율, 가격
            result = 0
            for i, e in enumerate(emoticons):
                if sale[i] * 100 >= a:
                    result += e * (1 - sale[i])

            if result >= b:
                cnt += 1
            else:
                total += result

        answer.append([cnt, total])

    answer.sort(reverse = True)

    return answer[0]