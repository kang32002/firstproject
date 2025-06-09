import streamlit as st

# 🎬 MBTI에 따른 영화 추천 데이터 (초기값)
if "mbti_data" not in st.session_state:
    st.session_state.mbti_data = {
        "INTJ": ["인터스텔라 🌌", "뷰티풀 마인드 🧠"],
        "INFP": ["이터널 선샤인 💫", "월터의 상상은 현실이 된다 ✈️"],
        "ENTP": ["인셉션 🧠", "마션 🚀"],
        "ISTP": ["프레스티지 🎩", "메멘토 🧠"],
        "ESFP": ["쥬라기 월드 🦖", "가디언즈 오브 갤럭시 🚀"],
        # 나머지도 필요하면 추가 가능!
    }

st.title("📽️ MBTI 과학·수학 명작 영화 추천기")
st.markdown("👇 아래에서 **MBTI를 선택하고**, 영화를 확인하거나 추가해보세요!")

# 🧠 MBTI 선택 드롭다운
mbti_list = list(st.session_state.mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", [""] + mbti_list)

if selected_mbti:
    st.markdown(f"### 🎥 {selected_mbti} 유형에게 추천되는 영화 리스트")
    for i, movie in enumerate(st.session_state.mbti_data[selected_mbti], start=1):
        st.write(f"{i}. 🍿 {movie}")

    st.markdown("---")
    st.markdown("#### ➕ 새로운 영화 추천 추가하기")
    
    new_movie = st.text_input("추가하고 싶은 영화 제목을 입력하세요 (예: 인사이드 아웃 🧠)")

    if st.button("✅ 추가하기"):
        if new_movie.strip():
            st.session_state.mbti_data[selected_mbti].append(new_movie.strip())
            st.balloons()
            st.success(f"🎉 '{new_movie}'(이)가 {selected_mbti}에 추가됐어요!")
        else:
            st.warning("⚠️ 공백이 아닌 제목을 입력해주세요!")
