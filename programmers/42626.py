import heapq


def solution(scoville, K):
    heap = []

    # 매번 정렬하는 비용을 줄이기 위해 Heap 사용
    for value in scoville:
        heapq.heappush(heap, value)

    count = 0

    # 가장 작은 값이 K보다 크면 반복 끝
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:  # 만약 인덱스 에러가 생길 경우(제한 사항을 만족시키지 못할 경우)
            return -1
        count += 1

    return count
