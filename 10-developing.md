# 개발형 코딩 테스트

- 정해진 목적에 따라 동작하는 완성된 프로그램을 개발하는 것을 요구하는 코딩 테스트 유형

| 알고리즘 코딩 테스트 | 개발형 코딩 테스트 |
| ----------------- | --------------- |
| 요구사항에 맞는 모듈 개발 | 완성도 높은 하나의 프로그램 개발 |
| 시간, 공간 복잡도 분석 | 모듈을 적절히 조합하는 능력 요구 |

- 일부 기업은 해커톤을 통해 채용
  - 단기간에 아이디어를 제품화 하는 프로젝트 이벤트
  - 대개 1~2일 정도 진행
  - 만든 프로그램을 시연하고 발표한 다음 채점을 진행

- 분야에 따라 상세 요구사항이 다를 수 있다.
  - 모바일 클라이언트: Android, iOS
  - 웹 서버: Spring, Django 등 서버 개발 프레임워크 사용
- 분야에 상관없이 꼭 알아야 하는 개념과 도구에 대해 학습할 필요가 있음
  - C-S, JSON, REST API, ...

## 서버와 클라이언트

- 클라이언트가 `요청`을 보내면 서버가 `응답`하는 구조

## HTTP

- 웹 문서를 주고받는데 사용
- 모바일 앱 및 게임 개발 등에서 특정 형식의 데이터를 주고 받는 용도로도 사용
- 클라이언트는 요청에 따라 적절한 HTTP 메서드를 사용하여 통신
  - GET, POST, PUT, DELETE

- 2020 카카오 2차 코딩테스트
  - 오프라인 코딩 테스트에서는 JSON format의 데이터를 응답하는 REST API를 활용해야하니, REST API 호출과 JSON format 데이터를 파싱해 활용할 수 있는 parser 코드를 미리 준비해오시길 바랍니다.

```py
import json
user = {
  "id": "112351251",
  "name": "taypark",
  "hobby": ["Music", "Drum"]
}

# JSON화
json_data = json.dumps(user, indent=4)
print(json_data)

# 파일화
with open("user.json", "w", encoding="utf-8") as file:
  json_data = json.dump(user, file, indent=4)

```

> 데이터를 받아와 이름만 처리하는 예제

```py
import requests

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

data = response.json()

name_list = []
for user in data:
  name_list.append(user['name'])

print(name_list)
```