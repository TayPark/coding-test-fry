# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

def solution(operations):
    queue = []
    
    for op in operations:
        instruction, value = op.split()
        if instruction == "I":
            queue.append(int(value))
        elif instruction == "D":
            if len(queue) == 0:
                continue
            if value == '1':
                queue.remove(max(queue))
            elif value == '-1':
                queue.remove(min(queue))

    if len(queue) == 0:
        return [0, 0]
    
    return [max(queue), min(queue)]