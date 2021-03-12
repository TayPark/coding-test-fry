# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while people:
        heavy = people.pop()
        if people and heavy + people[0] <= limit:
            people.popleft()
        answer += 1
    
    return answer