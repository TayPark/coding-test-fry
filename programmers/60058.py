# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

def divide(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return (p[:i + 1], p[i + 1:])
    return (p, '')


def balanced(p):
    stack = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    return True


def reorder(u):
    tmp = ''
    for i in u:
        if i == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp


def solution(p):
    if p == '':
        return ''

    u, v = divide(p)

    if not balanced(u):
        return '(' + solution(v) + ')' + reorder(u[1:-1])

    return u + solution(v)
