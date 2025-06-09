import streamlit as st

# 🎬 MBTI에 따른 영화 추천 데이터
mbti_movie_recommendations = {
    "INTJ": ["인터스텔라 🌌", "뷰티풀 마인드 🧠", "2001: 스페이스 오디세이 🚀"],
    "INTP": ["굿 윌 헌팅 📚", "테넷 🌀", "트랜센던스 🧬"],
    "ENTJ": ["소셜 네트워크 🌐", "아이언맨 🤖", "더 이미테이션 게임 🔐"],
    "ENTP": ["마션 🚀", "인셉션 🧠", "빅 히어로 🦾"],

    "INFJ": ["콘택트 👽", "어라이벌 🛸", "월-E 🌎"],
    "INFP": ["코다 🎶", "월터의 상상은 현실이 된다 ✈️", "이터널 선샤인 💫"],
    "ENFJ": ["페이첵 🧩", "허 허트 💻❤️", "업사이드 다운 🌍"],
    "ENFP": ["백 투 더 퓨처 ⏰", "루시 🧬", "닥터 스트레인지 🔮"],

    "ISTJ": ["더 매트릭스 🧪", "콘택트 👽", "큐브 🧊"],
    "ISFJ": ["패신저스 🚀", "그린 북 🚗", "플립 🔬"],
    "ESTJ": ["아폴로 13 🧑‍🚀", "머니볼 ⚾", "트론: 새로운 시작 💡"],
    "ESFJ": ["인터스텔라 🌌", "월-E 🌱", "인사이드 아웃 🧠"],

    "ISTP": ["메멘토 🧠", "프레스티지 🎩", "블레이드 러너 2049 🕶️"],
    "ISFP": ["허트 로커 💣", "루퍼 🔫", "애니홀 🎞️"],
    "ESTP": ["인디아나 존스 🔍", "에지 오브 투모로우 ⏳", "이퀼리브리엄 ⚖️"],
    "ESFP": ["쥬라기 월드 🦖", "나우 유 씨 미 🎩", "가디언즈 오브 갤럭시 🚀"]
}

# 🎈 제목
st.title("📽️ MBTI 과학·수학 명작 영화 추천기")

# 🎯 설명
st.markdown("당신의 **MBTI** 유형을 입력하면, 과학과 수학을 테마로 한 명작 영화를 추천해드릴게요! 💡🧬")

# 🎯 MBTI 입력
user_mbti = st.text_input("당신의 MBTI는 무엇인가요? (예: INFP, ESTJ 등)", "").upper()

# 🎉 추천 및 풍선 효과
if user_mbti:
    if user_mbti in mbti_movie_recommendations:
        st.balloons()  # 🎈풍선 효과

        st.success(f"🎉 {user_mbti} 유형에게 추천하는 영화들입니다!")
        for movie in mbti_movie_recommendations[user_mbti]:
            st.write(f"🍿 {movie}")
    else:
        st.warning("⚠️ 올바른 MBTI 유형을 입력해주세요! (예: INTJ, ENFP 등)")
