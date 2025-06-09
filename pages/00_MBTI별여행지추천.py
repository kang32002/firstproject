import streamlit as st

# 📦 세션 상태 초기화
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

if "ratings" not in st.session_state:
    st.session_state.ratings = {}  # {(mbti, movie): rating}

# 🎯 타이틀
st.title("📽️ MBTI 과학·수학 명작 영화 추천기 ⭐")

# 📍 설명
st.markdown("당신의 **MBTI**에 따라 명작 영화를 추천해드리고, 직접 추가도 가능하며 ⭐별점 평가도 할 수 있어요!")

# 🧠 MBTI 선택
mbti_list = list(st.session_state.movie_db.keys())
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요!", [""] + mbti_list)

if selected_mbti:
    st.subheader(f"🎞️ {selected_mbti} 추천 영화 리스트")

    # 🎬 기존 영화들 출력 + ⭐ 평점 평가
    for movie in st.session_state.movie_db[selected_mbti]:
        col1, col2 = st.columns([4, 2])
        with col1:
            st.write(f"🍿 {movie}")
        with col2:
            key = f"{selected_mbti}_{movie}"
            st.session_state.ratings[key] = st.slider(
                "⭐ 평점", 0, 5, st.session_state.ratings.get(key, 0),
                key=key
            )

    st.markdown("---")
    
    # ➕ 사용자 영화 추가
    st.subheader("➕ 영화 직접 추가하기")
    new_movie = st.text_input("새 영화 제목을 입력하세요 (이모지도 OK!)")

    if st.button("추가"):
        if new_movie.strip():
            if new_movie not in st.session_state.movie_db[selected_mbti]:
                st.session_state.movie_db[selected_mbti].append(new_movie)
                st.success(f"'{new_movie}'이(가) {selected_mbti} 추천 목록에 추가되었어요!")
            else:
                st.info(f"'{new_movie}'은(는) 이미 추천 목록에 있어요.")
        else:
            st.warning("❗ 공백은 추가할 수 없어요.")
