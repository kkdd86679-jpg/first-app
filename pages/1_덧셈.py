import streamlit as st
import random

st.title("➕ 덧셈 게임")
st.write("랜덤한 덧셈 문제를 풀어보세요. 정답을 입력하고 제출 버튼을 눌러 결과를 확인하세요.")

if "addition_question" not in st.session_state:
    st.session_state.addition_question = None
if "addition_answer" not in st.session_state:
    st.session_state.addition_answer = None
if "addition_score" not in st.session_state:
    st.session_state.addition_score = 0
if "addition_attempts" not in st.session_state:
    st.session_state.addition_attempts = 0


def make_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    return f"{a} + {b}", a + b

if st.button("새 문제 출제") or st.session_state.addition_question is None:
    st.session_state.addition_question, st.session_state.addition_answer = make_question()
    st.session_state.addition_user_answer = ""

st.subheader("문제")
st.write(f"**{st.session_state.addition_question} = ?**")
user_input = st.text_input("정답을 입력하세요", key="addition_user_answer")

if st.button("제출"):
    st.session_state.addition_attempts += 1
    try:
        user_value = int(user_input)
        if user_value == st.session_state.addition_answer:
            st.success("정답입니다! 🎉")
            st.session_state.addition_score += 1
        else:
            st.error(f"틀렸습니다. 정답은 {st.session_state.addition_answer}입니다.")
    except ValueError:
        st.warning("숫자를 입력해주세요.")

st.write(f"현재 점수: {st.session_state.addition_score}점")
st.write(f"도전 횟수: {st.session_state.addition_attempts}회")
