import os
from io import BytesIO
from tempfile import NamedTemporaryFile
from gtts import gTTS
import pygame


# 지정 경로의 음성파일을 재생합니다.
# macOS에서는 afplay 명령으로 오디오파일을 재생할 수 있지만,
# 윈도우에서는 OS 기본에서 지원되는 명령이 없기에
# pygame 라이브러리를 통해 재생토록 합니다.
def play_file(file_path: str) -> None:
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # 오디오 파일이 재생되는 동안 기다립니다.
    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.quit()
    
def say(message: str, lang: str) -> None:
    io = BytesIO()

    tts = gTTS(message, lang=lang)

    # 1) 파일 직접 저장없이 처리하고자 할 때에
    #    생성된 음성파일을 메모리 파일 객체에 저장합니다.
    # tts.write_to_fp(io)

    # 2) 음성파일 재생을 위해서는 파일에 저장해야합니다.
    with NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        try:
            tts.write_to_fp(f)
            f.close()
            play_file(f.name)
        finally:
            # 재생한 파일은 제거합니다.
            os.unlink(f.name)