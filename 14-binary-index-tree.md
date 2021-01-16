# 바이너리 인덱스 트리

어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1, 2, 3, 4, 5라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 된다. 그리고 그 상태에서 다섯번째 수를 2로 바꾸고 3번째부터 5번째 합을 구하라고 하면 12가 될 것이다.

- 데이터 수 N: 1 ~ 1,000,000
- 데이터 변경 수 M: 1 ~ 10,000
- 구간 합 계산 수 K: 1 ~ 10,000

## BIT

- 2진법 인덱스 구조를 활용해 구간 합 문제를 효과적으로 해결
  - 펜윅 트리(fenwick tree)라고도 한다.
- 0이 아닌 마지막 비트를 찾는 방법
  - 특정한 숫자 K의 0이 아닌 마지막 비트를 찾기 위해 K & -K를 계산

```py
# 각각 전체 데이터의 수, 변경 횟수, 구간 합 계산 횟수
n, m, k = map(int, input().split())
# 전체 데이터는 최대 1,000,000개
arr = [0] * (n + 1)
tree = [0] * (n + 1)
# i번째 수까지 누적 합을 계산
def prefix_sum(i):
  result = 0
  while i > 0:
    result += tree[i]
    i -= (i & -i)
# i번째 수를 diff만큼 더함
def update(i, diff) :
  while i <= n:
    tree[i] += diff
    i += (i & -i)
# start부터 end까지 구간합
def interval_sum(start, end):
  return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
  x = int(input())
  arr[i] = x
  update(i, x)

for i in range(m + k):
  a, b, c = map(int, input().split())
  if a == 1:  # 업데이트 연산인 경우
    update(b, c - arr[b]) # 바뀐 크기만큼 적용
    arr[b] = c
  else: # 구간합
    print(interval_sum(b, c))
```