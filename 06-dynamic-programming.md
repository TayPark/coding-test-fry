# 다이나믹 프로그래밍

- **메모리를 사용하여 수행 시간 효율성을 높이는 방법**
- 이미 계산된 결과는 별도의 메모리 영역에 저장(메모이제이션 또는 캐싱)하여 다시 계산하지 않도록 함
- **Top-down**, **Bottom-up** 방식
- 아래의 조건을 만족해야 함
  - `최적 부분 구조`
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아 합치면 해결
  - `중복되는 부분 문제`
    - 동일한 작은 문제를 반복적으로 해결

## 피보나치 수열

- a1과 a2를 주고 An = An-1 + An-2 의 점화식을 이용한 수열

```py
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
```

이 경우 같은 점화식이 여러번 호출될 수 있다. 그러므로 한 번 해결한 문제는 데이터에 저장하여 계산 시간을 줄일 수 있다.

### 하향식

```py
n = int(input())
memo = [0] * n

def fibo(x):
  if x == 1 or x == 2:
    return 1
  if memo[x] != 0:
    return memo[x]
  memo[x] = fibo(x - 1) + fibo(x - 2)
  return memo[x]

print(fibo(99))
```

### 상향식

```py
n = int(input())
memo = [0] * (n + 1)  # 리스트 초기화
memo[1] = 1 # 초기값 넣어줌
memo[2] = 1 

for i in range(3, n + 1): # 3번 인덱스부터 반복 수행
  memo[i] = memo[i - 1] + memo[i - 2] # 전체 수를 모두 기입

print(memo[n])

et = time.time()
```

## 다이나믹 프로그래밍 vs 분할정복

- 최적 부분 구조(큰 문제를 여러개의 작은 문제들로 나누어 해결)를 가질 때 사용
- 차이점은 **부분 문제의 중복 여부**
  - 다이나믹은 문제들이 중복될 수 있다.
  - 분할 정복은 중복되지 않는다.

## 다이나믹 프로그래밍 문제에 접근하는 방법

- 문제 유형이 적절한지 먼저 파악
- 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 먼저 검토
  - 다른 풀이 방법으로 떠오르지 않을 때 최후의 방법
- 재귀함수로 비효율적인 완전탐색 프로그램을 작성한 뒤에 하향식 다이나믹 프로그래밍이 가능하다면 코드를 개선하는 것도 방법

## 들키지 않고 식량 털기

> N개의 식량 창고가 있고, 각 식량창고에는 서로 다른 식량의 양이 존재한다. 도적은 식량 창고를 털어 식량을 확보하고자 한다. 이 때 인접한 식량창고를 털 수는 없다. 가장 많은 식량을 털기 위한 프로그램을 작성하라.

- 인접한 식량을 털 수는 없으므로, 현재 찾으려는 식량 창고로부터 -2까지의 식량창고 중 최대값을 고려한다.

```py
n = int(input()) # 식량 창고 수
array = list(map(int, input().split())) # 식량 창고마다의 식량 수

memo = [0] * n  # 초기화

memo[0] = array[0]
memo[1] = max(array[0], array[1])

for i in range(2, n):
  memo[i] = max(memo[i - 1], memo[i - 2] + array[i])

print(memo[n-1])
```

## 1로 만들기

> 정수 X가 주어졌을 때 정수 X에 사용할 수 있는 연산은 4개이다. 
- 5로 나누어 떨어지면 5로 나눈다.
- 3으로 나누어 떨어지면 3으로 나눈다.
- 2로 나누어 떨어지면 2로 나눈다.
- 1을 뺀다.
정수 X가 주어졌을 때 연산을 사용하여 1로 만드려 한다. 이 때 연산을 사용하는 횟수의 최소값을 출력하라.

해결
- 이 문제는 그리디 알고리즘으로 최적의 값을 구할 수 없다. 더 큰 수를 나누면 수가 빨리 줄어들기 때문이다.
- 그러므로 이 문제의 점화식은 **min(1빼기, 2로나누기, 3으로나누기, 5로나누기) + 1** 이 1이 될 때까지 수행하는 것이 최적이라 할 수 있다.
- 아래 소스코드는 상향식으로 프로그래밍했다.

```py
x = int(input())

memo = [0] * (x + 1)

# 0과 1은 고려하지 않으므로 인덱스는 2 ~ x
for i in range(2, x + 1):
  # 아래로 갈 수록 최적의 방법
  # 현재에서 1을 빼는 경우
  memo[i] = memo[i - 1] + 1
  # 현재에서 2를 나누는게 가능한 경우
  if i % 2 == 0:
    memo[i] = min(memo[i], memo[i // 2] + 1)
  # 현재에서 3를 나누는게 가능한 경우
  if i % 3 == 0:
    memo[i] = min(memo[i], memo[i // 3] + 1)
  # 현재에서 5를 나누는게 가능한 경우
  if i % 5 == 0:
    memo[i] = min(memo[i], memo[i // 5] + 1)

print(memo[x])
```

## 효율적인 화폐 구성

- N가지 종류의 화폐 갯수가 있는데, M원을 만들기 위한 최소 화폐 갯수를 구하라. 불가능하다면 -1을 출력하라.
- 이후의 N개 줄에는 화폐의 가치가 주어진다.
- ai = 금액 i를 만들 수 있는 최소한의 화폐 수
- k = 각 화폐의 단위
- 각 화폐의 단위인 k를 하나씩 확인하며
  - ai-k를 만드는 방법이 존재하는 경우, ai = min(ai, ai-k + 1)
  - ai-k를 만드는 방법이 존재하지 않는 경우, ai = INF(무한대)

```py
# n: 화폐 수, m: 목표 돈
n, m = map(int, input().split())

# 화폐 종류 입력 받음
array = []
for i in range(n):
  array.append(int(input()))

# 한번에 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [-1] * (m + 1)
dp[0] = 0

for i in range(n):  # 화폐 수 만큼
  for j in range(array[i], m + 1):  # 화폐 ~ 목표 금액
    if dp[j - array[i]] != -1:
      dp[j] = min(dp[j], dp[j - array[i]] + 1)

if dp[m] == -1:
  print(-1)
else:
  print(dp[m])
```

## 금광 채굴자

> N x M 크기의 금광이 있다. 금광은 1 x 1 크기의 칸으로 이루어져 있고, 칸에는 특정한 크기의 금이 있다. 채굴자는 첫 번째 열부터 출발하여 금을 캔다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다. 이후 m - 1번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야한다. 결과적으로 얻을 수 있는 금의 최대 크기를 출력하라.

입력
- 테스트 케이스 수
- n m
- n x m개 매장된 금의 갯수
- (반복)

해결 아이디어
- 채굴자는 오른쪽, 오른쪽 위, 오른쪽 아래로 이동하기 때문에, 반대로 금광 입장에서는 왼쪽 위, 왼쪽, 왼쪽 아래에서 온다고 생각하면 된다.
  - 금광 입장에서 최대로 금을 채굴할 수 있도록 매번 갱신한다.
- array[i][j] = i행 j열에 존재하는 금의 양
- dp[i][j] = i열 j행까지의 최적의 해(최대값)
- dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

```py
tc = int(input())

for i in range(tc):
  n, m = map(int, input().split())
  array = list(map(int, input().split()))
  # 2차원 DP 테이블 초기화
  dp = []
  index = 0
  for i in range(n):
    dp.append(array[index:index + m]) # 금광의 열 크기만큼 슬라이싱하여 2차원 배열 초기화
    index += m
  
  for j in range(1, m): # 매 열을 확인하며
    for k in range(n):  # 각 행들에 대해
      # 왼쪽 위에서 오는 경우
      if i == 0: left_up = 0
      else: left_up = dp[k-1][j - 1]
      # 왼쪽 아래에서 오는 경우
      if i == n - 1: left_down = 0
      else: left_down = dp[i + 1][j - 1]
      # 왼쪽 위에서 오는 경우
      left = dp[i][j - 1]
      # DP 테이블 업데이트
      dp[i][j] = dp[i][j] + max(left_up, left, left_down)
  
  result = 0
  for i in range(n):  # 전체 행 중에서
    result = max(result, dp[i][m - 1])  # 가장 큰 값
  print(result)
```

## 병사 배치하기

> N명의 병사가 일렬로 나열되어있다. 각 병사는 특정한 값의 전투력을 보유하고 있다. 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치를 하려 한다. 나열된 병사들의 전투력을 내림차순으로 만들기 위해서 중간의 병사를 열외시키려한다. 이 때 남아있는 병사의 수가 최대가 되는 열외 병사의 수를 구하라.

입력
- 병사 수 N
- 병사 리스트
출력
- 열외 병사 수
해결
- 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)
  - D[i] = array[i]를 마지막 원소르 갖는 부분 수열의 최대 길이
  - 모든 0 <= j < i에 대해 `D[i] = max(D[i], D[j] + 1) if array[j] < array[i]`
- 하나의 수열 array가 있을 때, 가장 길게 증가하는 부분이 있다.
- 여기서는 반대의 경우를 찾는다.

```py
n = int(input())
array = list(map(int, input().split()))

array.reverse()

# 1차원 DP 테이블 초기화
dp = [1] * n

# LIS 알고리즘 수행
for i in range(1, n): # 1 ~ n - 1
  for j in range(0, i): # 0 ~ i - 1
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)
# 전체에서 가장 길게 증가하는 부분 제거
print(n - max(dp))
```