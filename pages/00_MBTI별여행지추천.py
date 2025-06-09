import streamlit as st

# 🎬 초기 추천 영화 데이터 (딕셔너리 형태, 세션에서 유지됨)
if "movie_db" not in st.session_state:
    st.session_state.movie_db = {
        "INTJ": ["인터스텔라 🌌", "뷰티풀 마인드 🧠"],
        "INTP": ["굿 윌 헌팅 📚", "테넷 🌀"],
        "ENTJ": ["소셜 네트워크 🌐", "아이언맨 🤖"],
        "ENTP": ["마션 🚀", "인셉션 🧠"],
        "INFJ": ["어라이벌 🛸", "월-E 🌎"],
        "INFP": ["코다 🎶", "이터널 선샤인 💫"],
        "ENFJ": ["페이첵 🧩", "허 허트 💻❤️"],
        "ENFP": ["백 투 더 퓨처 ⏰", "닥터 스트레인지 🔮"],
        "ISTJ": ["더 매트릭스 🧪", "큐브 🧊"],
        "ISFJ": ["패신저스 🚀", "그린 북 🚗"],
        "ESTJ": ["아폴로 13 🧑‍🚀", "머니볼 ⚾"],
        "ESFJ": ["월-E 🌱", "인사이드 아웃 🧠"],
        "ISTP": ["메멘토 🧠", "블레이드 러너 2049 🕶️"],
        "ISFP": ["루퍼 🔫", "애니홀 🎞️"],
        "ESTP": ["인디아나 존스 🔍", "에지 오브 투모로우 ⏳"],
        "ESFP": ["쥬라기 월드 🦖", "가디언즈 오브 갤럭시 🚀"]
    }

# 🎯 타이틀
st.title("📽️ MBTI 과학·수학 명작 영화 추천기")
st.markdown("당신의 **MBTI**를 선택하고, 맞춤 영화 추천도 받고 🎬 직접 영화도 추가해보세요! 🎉")

# 🧠 MBTI 선택
mbti_list = list(st.session_state.movie_db.keys())
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요!", [""] + mbti_list)

# ✅ MBTI가 선택된 경우
if selected_mbti:
    st.balloons()
    st.subheader(f"🍿 {selected_mbti} 유형 추천 영화 리스트")
    
    # 기존 영화 출력
    for movie in st.session_state.movie_db[selected_mbti]:
        st.write(f"🎞️ {movie}")

    st.markdown("---")
    
    # 🎁 사용자 입력창: 영화 추가
    new_movie = st.text_input("➕ 추천 영화 추가하기 (이모지도 자유롭게!)")
    if st.button("영화 추가"):
        if new_movie.strip():
            st.session_state.movie_db[selected_mbti].append(new_movie.strip())
            st.success(f"✅ 영화 '{new_movie}'가 {selected_mbti}에 추가됐어요!")
        else:
            st.warning("⚠️ 공백은 추가할 수 없어요!")
