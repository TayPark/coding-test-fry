# 우선순위 큐와 힙

- 우선순위가 가장 높은 데이터를 먼저 삭제하는 자료구조
- 우선순위에 따라 처리하고 싶을 때 사용
  - 숫자가 낮은 데이터를 우선순위가 높다고 가정
  - 파이썬의 경우 튜플의 맨 처음 데이터를 보고 판단
- 우선순위 큐 구현 방법
  - 리스트를 이용하는 방법
  - 힙을 이용하는 방법
- 데이터의 개수가 N개일 때, 구현 방식에 따라 시간 복잡도를 비교한다면 다음과 같다.

| 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
| ------------------ | ------- | -------- |
| 리스트              | O(1)    | O(N)     |
| 힙                 | O(logN) | O(logN)  |

- 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일하다(힙정렬)

## 힙의 특징

- `완전 이진트리`
- 항상 루트 노드를 제거
- 최소 힙: 루트가 가장 작은 값을 가짐
- 최대 힙: 루트가 가장 큰 값을 가짐
- iterable 자료구조를 최소 힙에 넣었다가 모두 빼면 힙정렬이 된 상태로 나온다.

```py
import sys
import heapq

def heapsort(arr):
  h = []
  result = []

  for value in arr:  # 전체 리스트를 힙에 추가
    heapq.heaqpush(h, value) 
  for i in range(len(h)): # 힙에서 전체 리스트 
    result.append(heapq.heappop(h))
  return result # pop

n = int(input())
array = []

for i in range(n):
  array.append(int(input())

res = heapsort(array)

for i in range(n):
  print(res[i])
```