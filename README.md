# pystudy

파이썬과 OpenAI API, Streamlit 등을 활용한 다양한 실습 예제 모음입니다.

## 주요 파일 설명

- `01-cli.py` : 파이썬 기본 CLI 예제
- `02-cli.py` : OpenAI API를 활용한 간단한 텍스트 생성 예제
- `03-cli.py` : 얼굴 특징을 입력받아 AI 관상 분석 결과 출력
- `04-webapp.py` : Streamlit 기반 관상 분석 웹앱
- `05-cli-streaming.py` : OpenAI API 스트리밍 응답 예제
- `06-cli-chat.py` : 영어 상황극 챗봇 CLI
- `07-json.py` : 멜론 TOP100 JSON 데이터 파싱 예제
- `08-webapp-melon-top100.py` : 멜론 TOP100 곡 목록 웹앱
- `09-melon-search.py` : 멜론 검색 API 활용 예제
- `ai.py` : OpenAI 기반 관상 분석 함수 구현
- `audio.py` : gTTS와 pygame을 활용한 음성 합성 및 재생
- `generater_01.py` : 파이썬 generator 예제

## 설치 방법

```sh
pip install -r requirements.txt
```

## 실행 방법

예시) 관상 분석 CLI 실행
```sh
python 03-cli.py
```

예시) 관상 분석 웹앱 실행
```sh
streamlit run 04-webapp.py
```

## 환경 변수

OpenAI API 사용을 위해 `.env` 파일에 아래와 같이 API 키를 설정하세요.

```
OPENAI_API_KEY=your_openai_api_key
```

## 참고

- [requirements.txt](requirements.txt) 파일을 참고하여 필요한 라이브러리를 설치하세요.
- 일부 예제는 인터넷