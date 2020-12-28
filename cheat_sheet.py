###
# 캐스팅
###
string = '1234'
print(int(string)) # 숫자 1234

integer = 1234
print(str(integer)) # 문자열 1234

###
# 숫자 0부터 N까지 리스트 만들기
###
num_list = list(range(50))
print(num_list) # [0, 1, 2, 3, 4, ...]

###
# 알파벳인지 확인
###
char = 'a'
if char.isalpha():
  print(True) # True

###
# 리스트를 문자로 합치기
###
str_arr = ['a', 'b', 'c', 'd', 'e']
print(''.join(str_arr)) # abcde

###
# 2차원 배열
###
# 만들지 마라. 뇌속으로 생각해라.

###
# 표준 입력 처리 
###
# 11 22 33 44 55 를 받는다고 가정
score_data = list(map(int, input().split())) # [11, 22, 33, 44, 55]
# 3개의 정수를 한번에 a, b, c에 저장
a, b, c = map(int, input().split()) # 1, 2, 3
# 101101 -> [1, 0, 1, 1, 0, 1]
each_num = list(map(int, input()))