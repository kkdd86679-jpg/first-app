import streamlit as st
import random

st.title("➗ 나눗셈 게임")
st.write("랜덤한 나눗셈 문제를 풀어보세요. 몫이 정수인 문제를 출제합니다.")

if "division_question" not in st.session_state:
    st.session_state.division_question = None
if "division_answer" not in st.session_state:
    st.session_state.division_answer = None
if "division_score" not in st.session_state:
    st.session_state.division_score = 0
if "division_attempts" not in st.session_state:
    st.session_state.division_attempts = 0


def make_question():
    b = random.randint(2, 12)
    c = random.randint(2, 12)
    a = b * c
    return f"{a} ÷ {b}", c

if st.button("새 문제 출제") or st.session_state.division_question is None:
    st.session_state.division_question, st.session_state.division_answer = make_question()
    st.session_state.division_user_answer = ""

st.subheader("문제")
st.write(f"**{st.session_state.division_question} = ?**")
user_input = st.text_input("정답을 입력하세요", key="division_user_answer")

if st.button("제출"):
    st.session_state.division_attempts += 1
    try:
        user_value = int(user_input)
        if user_value == st.session_state.division_answer:
            st.success("정답입니다! 🎉")
            st.session_state.division_score += 1
        else:
            st.error(f"틀렸습니다. 정답은 {st.session_state.division_answer}입니다.")
    except ValueError:
        st.warning("숫자를 입력해주세요.")

st.write(f"현재 점수: {st.session_state.division_score}점")
st.write(f"도전 횟수: {st.session_state.division_attempts}회")
