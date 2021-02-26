# https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque


def solution(numbers, target):
    answer = 0

    stack = deque([(0, 0)])  # 초기값, 사용할 numbers의 인덱스

    while stack:
        current_sum, num_idx = stack.popleft()  # 하나씩 꺼내서

        if num_idx == len(numbers):  # 사용한 숫자가 사용하려는 숫자의 수와 같고
            if current_sum == target:   # 타겟 넘버와 같으면
                answer += 1
        else:
            number = numbers[num_idx]
            # 더하거나 뺄 수 있으므로 2개를 넣음
            stack.append((current_sum + number, num_idx + 1))
            stack.append((current_sum - number, num_idx + 1))

    return answer
