# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def find_nearest(matched, current):
    for i in range(0, len(matched)):
        if matched[current + i] == False:
            return current + i
        elif matched[current - i] == False:
            return current - i


def solution(name):
    if name.count("A") == len(name):
        return 0

    answer = 0
    trans = "A" * len(name)
    matched = []

    for i in range(len(name)):
        if name[i] == trans[i]:
            matched.append(True)
        else:
            matched.append(False)

    pos = 0
    while True:
        answer += abs(pos - find_nearest(matched, pos))  # 가장 가까운 A가 아닌 곳으로 이동
        pos = find_nearest(matched, pos)
        matched[pos] = True

        go_left = ord(name[pos]) - ord("A")
        go_right = ord("Z") + 1 - ord(name[pos])
        if go_left >= go_right:
            answer += go_right
        else:
            answer += go_left
        if False not in matched:
            break

    return answer
