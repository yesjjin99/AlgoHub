def solution(wallpaper):
    answer = [50, 50, 0, 0]
    for i, wall in enumerate(wallpaper):
        for j, w in enumerate(wall):
            if w == '#':
                answer[0] = min(i, answer[0])
                answer[1] = min(j, answer[1])
                answer[2] = max(i + 1, answer[2])
                answer[3] = max(j + 1, answer[3])
    return answer
