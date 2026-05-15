import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="wide")

# 헤더
st.title("👤 자기소개")
st.divider()

# 프로필 섹션
st.subheader("기본 정보")
st.write("**이름:한윤우**")
st.write("**직책/직무:학생**")
st.write("**소속:청주교육대학교 교육학과**")

st.divider()

# 소개글 섹션
st.subheader("📝 소개")
st.write("안녕하세요? 저는 청주교육대학교 교육학과 한윤우라고 합니다. 만나서 반갑습니다.")

st.divider()

# 좋아하는 것 섹션
st.subheader("❤️ 좋아하는 것")
st.write("농구, 야구, 노래듣기, 파스타, 자동차.")

st.divider()

# 경력 / 프로젝트 섹션
st.subheader("💼 경력 및 프로젝트")
st.write("프로젝트 또는 경력사항을 추가해주세요.")

st.divider()

# 연락처 섹션
st.subheader("📧 연락처")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**이메일:** hanyoonwoo1121@gmail.com")

with col2:
    st.write("**GitHub:** [링크](https://github.com)")

with col3:
    st.write("**LinkedIn:** [링크](https://linkedin.com)")
