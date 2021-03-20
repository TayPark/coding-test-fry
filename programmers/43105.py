# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    for i in range(1, len(triangle)): # 윗 층부터
        for j in range(i + 1):  # 모든 숫자에 대해
            if j == 0:  # 대각선 라인(좌)
                triangle[i][j] += triangle[i - 1][j]
            elif j == i: # 대각선 라인(우)
                triangle[i][j] += triangle[i - 1][j - 1]
            else: # 나머지 숫자들에 대해
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    
    return max(triangle[-1])