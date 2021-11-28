# https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3

def solution(numbers):
    answer = [k for k in range(10) if k not in numbers]
    return sum(answer)