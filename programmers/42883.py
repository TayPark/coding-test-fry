# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number, k):
    stack = [number[0]]
    
    for num in number[1:]:
        # 더 큰 수를 찾았다면
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
        
    # 최선의 방법을 찾지 못했다면 앞에서부터 끊음
    if k != 0:
        stack = stack[:-k]
        
    return ''.join(stack)
