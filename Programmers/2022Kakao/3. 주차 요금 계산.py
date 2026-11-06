from math import ceil

def solution(fees, records):
    answer = []
    record = {}

    for r in records:
        time, n, f = r.split()
        time = int(time.split(':')[0]) * 60 + int(time.split(':')[1])

        if f == "IN":
            if n not in record:
                record[n] = [-time, False]
            else:
                record[n][0] -= time
                record[n][1] = False
        elif f == "OUT":
            record[n][0] += time
            record[n][1] = True

    for k in record.keys():
        if not record[k][1]:  # 입차된 후 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
            record[k][0] += 23 * 60 + 59
            record[k][1] = True

        if record[k][0] <= fees[0]:
            answer.append((k, fees[1]))  # 누적 주차 시간이 기본 시간 이하라면, 기본 요금 청구
        else:
            answer.append((k, fees[1] + ceil((record[k][0] - fees[0]) / fees[2]) * fees[3]))

    answer.sort()

    return [i[1] for i in answer]