# 정렬

## 선택 정렬

- 선택 정렬은 첫 인덱스부터 차례대로 가장 작은 값을 리스트에서 찾아 바꾸는 정렬 방법이다.
- 정렬을 위한 추가적인 공간이 필요하지 않다.
- O(n^2)이다.

```py
sort_me = list(map(int, input().split())) # 정렬할 리스트

for i in range(len(sort_me)): # 전체 리스트에서
  mini = sort_me[i] # 바꿀 자리의 값을 최소값이라고 가정하고
  pos = i   # 해당 인덱스를 가지고있는다.
  for j in range(i, len(sort_me)):  # 정렬되지 않은 리스트들에 대해
    if sort_me[j] < mini: # 더 작은 값이 있다면
      mini = sort_me[j] # 최소값을 바꾸고
      pos = j # 해당 인덱스를 저장한다.
  if pos != i:  # 최소값을 찾은 후 변동이 없다면
    sort_me[pos], sort_me[i] = sort_me[i], sort_me[pos]   # 스왑한다.

print(sort_me)
```

## 삽입 정렬

- 삽입 정렬은 인덱스를 거칠 때마다 이미 정렬된 리스트들 중 적절한 위치에 삽입하는 방법이다.
- 선택 정렬에 비해 난이도가 높지만 일반적으로 더 효율적으로 동작한다.
- O(n^2)이다.

```py
array = list(map(int, input().split()))

for i in range(1, len(array)): # 첫 인덱스는 생략한다.
  for j in range(i, 0, -1): # 지금 위치로부터 반대로 이동
    if array[j] < array[j-1]: # 현재 인덱스가 그 이전보다 작다면
      array[j], array[j-1] = array[j-1], array[j] 
    else: # 적절한 위치를 찾으면
      break

print(array)
```

## 퀵 정렬

- 일반적인 상황에서 가장 많이 사용하는 방법
  - 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 기준 데이터(pivot)을 설정하고 그 기준보다 큰 데이터와 작은 데이터를 위치를 바꾸는 방법
  - 첫 번째 데이터를 기준 데이터로 설정
- 퀵정렬은 평균 O(NlogN)의 복잡도를 갖는다
  - 최악의 경우(이미 정렬이 되어있는 데이터에 대해)는 O(N^2)를 갖는다.

```py
array = list(map(int, input().split()))

def quick(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[pivot] <= array[right]:
      right -= 1
    if left <= right:
      array[left], array[right] = array[right], array[left]
    else:
      array[pivot], array[right] = array[right], array[pivot]
  quick(array, 0, right - 1)
  quick(array, right + 1, end)

quick(array, 0, len(array) - 1)
print(array)
```

> 파이썬의 리스트 슬라이싱을 이용한 버전

```py
array = list(map(int, input().split()))

def quick(array):
  if len(array) <= 1:
    return array

  pivot = array[0]  # 피봇 설정
  rest = array[1:]  # 피봇을 제외한 리스트

  left_side = [x for x in rest if x <= pivot]
  right_side = [x for x in rest if x > pivot]

  return quick(left_side) + [pivot] + quick(right_side)

sorted = quick(array)
print(sorted)

```

## 계수 정렬

- 특정 조건 하에서 사용이 가능하지만 매우 빠르게 동작
  - 데이터 크기 범위가 제한되어 일종의 K-V(값 - 갯수)형태로 표현할 수 있을 때
- 데이터의 개수가 N, 데이터(양수) 중 최대값이 K일 때 O(N + K) 보장
- **동일한 데이터가 여러 개 등장할 때 효과적**
  - 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있다.
    - 데이터의 범위가 너무 넓거나(N이 커짐) 특정 영역으로 몰려있을 경우 비효율적

```py
array = list(map(int, input().split()))

count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')

```

> 파이썬 for문을 이용하는 방법

```py
# 입력
array = list(map(int, input().split()))
# 초기화
count = [0] * (max(array) + 1)

for i in array:
  count[i] += 1

# print(count)

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
```

## 두 배열의 원소 교체

- 두 배열 A와 B를 가지고있다. N개의 자연수 원소를 가진다.
- 배열 A와 B의 원소에 대해 최대 K번의 바꿔치기 연산을 수행할 수 있다.
- 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
- N, K, A, B 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 원소 합의 최대값을 출력하는 프로그램을 작성하라
  - A는 올림차순, B는 내림차순으로 정렬하고 서로 끝만 바꿔치기 하면 될듯?

- 입력 예시
  - 5 3 (N K)
  - 1 2 5 4 3 (A)
  - 5 5 6 6 5 (B)

- 출력예시
  - 26

```py
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))
```