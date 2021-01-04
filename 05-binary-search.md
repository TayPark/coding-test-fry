# 이진 탐색

- 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 확인
- 이진 탐색: **정렬되어 있는 리스트**에서 탐색 범위를 좁혀가며 데이터를 탐색
  - 시작, 끝, 중간점을 이용하여 탐색 범위 설정
- 단계마다 탐색 범위를 2로 나누는 것과 동일, 연산 횟수는 logN에 비례
  - 시간 복잡도는 O(logN)

```py
array = list(map(int, input().split()))
target = int(input())

array.sort()

def binary(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2  # 소수점 버림

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary(array, target, start, mid - 1)
  else:
    return binary(array, target, mid + 1, end)

result = binary(array, target, 0, len(array) - 1)

print(result)
```

## 파이썬 이진 탐색 라이브러리

```py
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))  # 정렬을 유지하며 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환 - 2
print(bisect_right(a, x)) # 정렬을 유지하며 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환 - 4
```

## 정렬된 배열에서 특정 수의 개수 구하기

입력
- 데이터의 수 N, 찾으려는 수 x
- 리스트
출력
- 찾으려는 수의 갯수 

```py
from bisect import bisect_left, bisect_right

array = list(map(int, input().split()))
target = int(input())

array.sort()

def count_num(array, left, right):
  left_index = bisect_left(array, left)
  right_index = bisect_right(array, right)
  return right_index - left_index

print(count_num(array, 1, 4)) # 1 <= x <= 4 인 x 갯수. 
```

## 파라메트릭 서치

- 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
  - 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

## 떡볶이 떡 만들기

> 절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위 부분이 잘리고 낮은 떡은 잘리지 않는다. 예를 들어 높이가 19, 14, 10, 17인 떡이 있고 높이가 15면 잘린 떡은 4, 0, 0, 2 이고 남은 떡은 15, 14, 10, 15이다. 손님이 가져가는 떡의 길이는 6이된다. 손님이 요청한 총 길이가 M일 때 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값은?

- 최대 10억의 길이, 효율적인 알고리즘 필요
- 입력 예시
  - 4 6 (떡의 개수 N, 떡의 길이 M)
  - 19 15 10 17 (떡의 개별 높이)
- 출력
  - 15

0. 데이터의 크기가 크다. 효율적인 알고리즘을 위해 이진 탐색을 사용한다.
1. 0과 가장 큰 떡의 길이 사이에서 이진 탐색을 수행한다. 중간값으로 떡을 잘랐을 때 적절한 길이가 될 때까지 이진 탐색을 수행한다.

```py
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)  # 가장 큰 값 저장
result = 0

while start <= end: # 
  total = 0 # 자른 전체 떡 길이
  mid = (start + end) // 2  # 절단기 값

  for x in array:
    if x > mid:
      total += x - mid  # 자른 떡 길이에 추가

  if total < m: # 요청양보다 적으면
    end = mid - 1

  else: # 요청양보다 크거나 같다면
    result = mid
    start = mid + 1

print(result)
```