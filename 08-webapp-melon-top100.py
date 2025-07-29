import streamlit as st
import requests
import webbrowser

st.set_page_config(page_title="Melon 2023-12-04")

st.title("Melon 2023-12-04")

# 데이터 가져오기
@st.cache_data
def fetch_song_list():
    url = "https://pyhub.kr/melon/20231204.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

songs = fetch_song_list()

# 리스트 출력
for song in songs:
    with st.container():
        cols = st.columns([1, 5])
        with cols[0]:
            st.image(song["커버이미지_주소"], width=48)
        with cols[1]:
            # 곡명을 버튼으로 만들어 클릭 시 웹 브라우저 열기
            if st.button(song['곡명'], key=f"btn_{song['곡일련번호']}"):
                # Melon 곡 상세 페이지로 이동
                url = f"https://www.melon.com/song/detail.htm?songId={song['곡일련번호']}"
                webbrowser.open_new_tab(url)
            st.markdown(f"좋아요: {song['좋아요']}")