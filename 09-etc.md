# 기타 알고리즘

## 소수 판별

- 소수: 자연수 중에서 1과 자기 자신을 제외한 자연수로 나누어떨어지지 않는 자연수

```py
def is_prime_number(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

print(is_prime_number(4)) # False
print(is_prime_number(7)) # True
```

- 2부터 X-1까지 모든 자연수에 대해 연산을 수행해야 한다.
  - 모든 수를 하나씩 확인해야 한다는 점에서 시간 복잡도는 O(X)이다.

## 약수의 성질

- 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있다.
  - 16의 약수 1, 2, 4, 8, 16
  - 2 * 8 = 8 * 2 = 16. 즉, 대칭을 이룬다.
- 특정한 자연수의 모든 약수를 찾을 때 **가운데 약수(제곱근)까지만 확인**하면 된다.

```py
import math

def is_prime_number(x):
  for i in range(2, int(math.sqrt(x)) + 1): # 제곱근까지만 확인
    if x % i == 0:
      return False
  return True
```

- 2부터 X의 제곱근 까지의 모든 자연수에 대해 연산을 수행한다.
  - 시간 복잡도는 O(root(N)) 이다.

## 다수의 소수 판별, 에라토스테네스의 체

- N보다 작거나 모든 소수를 찾을 때 사용
1. 2부터 N까지의 모든 자연수를 나열
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거(i는 제거하지 않음)
4. 더 이상 반복할 수 없을 때까지 2와 3을 반복

```py
import math

n = int(input())

array = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i * j] = False
      j += 1

# 모든 소수 출력
for i in range(2, n + 1):
  if array[i]:
    print(i, end=' ')
```

- **다수의 소수를 찾을 때 효과적으로 사용**
  - 각 자연수에 대한 소수 여부를 저장해야 하므로 메모리가 많이 필요
  - `10억`까지의 수는 불가능
- 선형 시간에 가까울 정도로 빠른 편
  - O(NloglogN)

## Two Pointers

- 리스트에 순차적으로 접근해야 할 때 두개의 점 위치를 기록하면서 처리하는 알고리즘
- 2, 3, 4, 5, 6, 7을 지목할 때 2~7이라고 하는것과 비슷
- 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 `시작`과 `끝점`으로 접근할 데이터의 범위를 표현

## 특정한 합을 가지는 부분 연속 수열 찾기

- N개의 자연수로 구성된 수열이 있다.
- 합이 M인 부분 연속 수열의 개수는?
1. 시작점(`start`)과 끝점(`end`)이 첫 번째 원소의 인덱스를 가리키도록 한다.
2. 현재 부분합이 M과 같다면 카운트한다.
3. 현재 부분합이 M보다 작다면 `end`를 증가시킨다.
4. 현재 부분합이 M보다 크거나 같다면 `start`를 1 증가시킨다.
5. 모든 경우를 확인할 때까지 2~4 과정을 반복한다.

```py
n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
  while interval_sum < m and end < n:
    interval_sum += data[end]
    end += 1
  if interval_sum == m:
    count += 1
  interval_sum -= data[start]
```

## 구간 합 문제

- 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
- {10, 20, 30, 40, 50}
  - 두 번째 부터 네 번째 까지 = 20 + 30 + 40 + 50

## 구간 합 빠르게 계산하기

- N개의 정수를 가진 수열이 있다.
- M개의 쿼리 정보가 주어진다.
  - Left 또는 Right로 구성된다.
  - 각 쿼리에 대해 [Left, Right] 구간에 포함된 데이터들의 합을 출력
- 수행 제한 시간은 O(N + M)

## Prefix Sum

- 배열의 맨 앞부터 특정 위치까지 합을 미리 구해놓은 것
  - N 개의 수 위치 각각에 대해 Prefix sum을 구해 P에 저장
  - 매 M개의 쿼리 정보를 확인할 때 구간 합은 `P[Right] - P[Left - 1]`이다.

```py
n = list(map(int, input().split()))

# prefix 초기화
prefix_sum = [0]
sum_value = 0
for i in n:
  sum_value += i
  prefix_sum.append(sum_value)

a, b = map(int, input().split())

print(prefix_sum[b] - prefix_sum[a-1])

```