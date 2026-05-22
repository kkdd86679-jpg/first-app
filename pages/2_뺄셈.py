import streamlit as st
import random

st.title("➖ 뺄셈 게임")
st.write("랜덤한 뺄셈 문제를 풀어보세요. 정답을 입력하고 제출 버튼을 눌러 결과를 확인하세요.")

if "subtraction_question" not in st.session_state:
    st.session_state.subtraction_question = None
if "subtraction_answer" not in st.session_state:
    st.session_state.subtraction_answer = None
if "subtraction_score" not in st.session_state:
    st.session_state.subtraction_score = 0
if "subtraction_attempts" not in st.session_state:
    st.session_state.subtraction_attempts = 0


def make_question():
    a = random.randint(20, 80)
    b = random.randint(1, a)
    return f"{a} - {b}", a - b

if st.button("새 문제 출제") or st.session_state.subtraction_question is None:
    st.session_state.subtraction_question, st.session_state.subtraction_answer = make_question()
    st.session_state.subtraction_user_answer = ""

st.subheader("문제")
st.write(f"**{st.session_state.subtraction_question} = ?**")
user_input = st.text_input("정답을 입력하세요", key="subtraction_user_answer")

if st.button("제출"):
    st.session_state.subtraction_attempts += 1
    try:
        user_value = int(user_input)
        if user_value == st.session_state.subtraction_answer:
            st.success("정답입니다! 🎉")
            st.session_state.subtraction_score += 1
        else:
            st.error(f"틀렸습니다. 정답은 {st.session_state.subtraction_answer}입니다.")
    except ValueError:
        st.warning("숫자를 입력해주세요.")

st.write(f"현재 점수: {st.session_state.subtraction_score}점")
st.write(f"도전 횟수: {st.session_state.subtraction_attempts}회")
