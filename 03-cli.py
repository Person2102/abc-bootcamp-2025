from ai import get_personality_analysis
from dotenv import load_dotenv

load_dotenv() # .env 파일이 있다면, 환경변수로서 로딩

print("# AI 관상가입니다. 얼굴 특징을 입력해주시면 성격과 미래를 전망해드릴게요.")
line = input("얼굴 특징: ").strip()

if not line:
    print("에러: 얼굴 특징을 입력하지 않으셨습니다.")
else:
    print("입력하신 얼굴 특징:", line)
    print("분석 중...")
    result = get_personality_analysis(line)
    print("분석 완료!")
    print(result)
