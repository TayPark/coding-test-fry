# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

def solution(begin, target, words):
    if target not in words:
        return 0
    visited, stacks = [begin], [begin]
    answer = 0
    while stacks:
        stack = stacks.pop()
        for word in words:
            count = 0
            for s, w in zip(stack, word):
                if s != w:
                    count += 1
            if count == 1:  # 하나만 다른 단어에 대해서
                if word not in visited:  # 이미 방문한 단어가 아닐 때
                    if word == target:  # 같으면 +1하고 리턴
                        return answer + 1
                    visited.append(word)
                    stacks.append(word)
        answer += 1
    return answer
