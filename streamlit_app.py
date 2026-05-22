import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="wide")

# 헤더
st.title("👤 자기소개")
st.write("반갑습니다!")
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

# 연락처 섹션
st.subheader("📧 연락처")
st.write("**이메일:** hanyoonwoo1121@gmail.com")

st.divider()

# 사칙연산 게임 섹션
st.subheader("🎮 사칙연산 게임")
st.write("간단한 계산 문제를 풀어보세요. 10초 안에 빠르게 풀어야 합니다! ⏲️")

import random
import time
import math

st.markdown(
    """
    <style>
    @keyframes blink {
      0% { opacity: 1; }
      50% { opacity: 0.2; }
      100% { opacity: 1; }
    }
    .timer-normal { font-size: 1.1rem; margin-bottom: 0.4rem; }
    .timer-danger { color: #ff3b30; font-weight: bold; animation: blink 1s infinite; }
    </style>
    """,
    unsafe_allow_html=True,
)

TIME_LIMIT = 10

if "score" not in st.session_state:
    st.session_state.score = 0
if "question" not in st.session_state:
    st.session_state.question = None
if "answer" not in st.session_state:
    st.session_state.answer = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "timeout_expired" not in st.session_state:
    st.session_state.timeout_expired = False


def new_question():
    operators = ["+", "-", "×", "÷"]
    num_terms = random.choice([2, 3])
    if num_terms == 2:
        op = random.choice(operators)
        if op == "+":
            a = random.randint(20, 120)
            b = random.randint(10, 120)
            expr = f"{a} + {b}"
        elif op == "-":
            a = random.randint(20, 120)
            b = random.randint(10, a)
            expr = f"{a} - {b}"
        elif op == "×":
            a = random.randint(8, 18)
            b = random.randint(8, 18)
            expr = f"{a} × {b}"
        else:
            b = random.randint(2, 15)
            c = random.randint(2, 10)
            expr = f"{b * c} ÷ {b}"
    else:
        op1 = random.choice(operators)
        op2 = random.choice(operators)
        a = random.randint(10, 80)
        b = random.randint(2, 20)
        c = random.randint(2, 20)
        if op1 == "÷":
            a = b * random.randint(2, 8)
        if op2 == "÷":
            c = random.randint(2, 12)
            b = c * random.randint(2, 8)
        expr = f"{a} {op1} {b} {op2} {c}"

    result = eval(expr.replace("×", "*").replace("÷", "/"))
    if isinstance(result, float) and abs(result - round(result, 2)) < 1e-9:
        result = round(result, 2)
    return expr, result

if st.button("새 문제 출제") or st.session_state.question is None:
    st.session_state.question, st.session_state.answer = new_question()
    st.session_state.start_time = time.time()
    st.session_state.timeout_expired = False
    if "user_answer" in st.session_state:
        st.session_state.user_answer = ""

elapsed = 0.0
if st.session_state.start_time is not None:
    elapsed = time.time() - st.session_state.start_time
remaining = max(0, math.ceil(TIME_LIMIT - elapsed))
progress_value = min(100, max(0, int(elapsed / TIME_LIMIT * 100)))

st.write(f"**문제:** {st.session_state.question}")
start_ts = st.session_state.start_time if st.session_state.start_time is not None else time.time()

components.html(
    f"""
    <style>
      .timer-box {{ width: 100%; max-width: 420px; margin-bottom: 16px; }}
      .timer-label {{ font-size: 1rem; margin-bottom: 8px; color: #333; }}
      .timer-clock {{ font-size: 2rem; font-weight: 700; margin-bottom: 8px; }}
      .timer-clock.danger {{ color: #ff3b30; animation: blink 0.8s infinite; }}
      .timer-bar {{ width: 100%; height: 16px; background: #e3e3e3; border-radius: 12px; overflow: hidden; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); }}
      .timer-fill {{ height: 100%; width: 100%; background: linear-gradient(90deg, #4caf50 0%, #9c27b0 100%); transition: width 0.2s ease; }}
      .timer-note {{ margin-top: 8px; font-size: 0.95rem; color: #555; }}
      @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.2; }} 100% {{ opacity: 1; }} }}
    </style>
    <div class="timer-box">
      <div class="timer-label">⏲️ 남은 시간</div>
      <div id="timerClock" class="timer-clock">{remaining}초</div>
      <div class="timer-bar"><div id="timerFill" class="timer-fill"></div></div>
      <div id="timerNote" class="timer-note"></div>
    </div>
    <script>
      const startTime = {start_ts};
      const timeLimit = {TIME_LIMIT};
      const clock = document.getElementById('timerClock');
      const fill = document.getElementById('timerFill');
      const note = document.getElementById('timerNote');
      function updateTimer() {{
        const elapsed = (Date.now() / 1000) - startTime;
        const remaining = Math.max(0, timeLimit - elapsed);
        const seconds = Math.ceil(remaining);
        const percent = Math.max(0, Math.min(100, remaining / timeLimit * 100));
        clock.textContent = seconds + '초';
        fill.style.width = percent + '%';
        if (seconds <= 3 && seconds > 0) {{
          clock.classList.add('danger');
          note.textContent = '3초 이내! 서둘러 입력하세요.';
        }} else {{
          clock.classList.remove('danger');
          note.textContent = remaining > 0 ? '문제를 풀고 제출해보세요.' : '시간 초과! 새 문제를 눌러 다시 도전하세요.';
        }}
      }}
      updateTimer();
      setInterval(updateTimer, 200);
    </script>
    """,
    height=170,
)

if elapsed >= TIME_LIMIT:
    st.warning("시간 초과! 새 문제를 눌러 다시 도전하세요.")
    st.session_state.timeout_expired = True

user_input = st.text_input("정답을 입력하세요", key="user_answer")

if st.button("제출"):
    if st.session_state.start_time is None:
        st.info("먼저 새 문제 출제를 눌러주세요.")
    elif st.session_state.timeout_expired or time.time() - st.session_state.start_time > TIME_LIMIT:
        st.error("시간이 초과되었습니다. 새 문제를 눌러 다시 시작하세요.")
        st.session_state.timeout_expired = True
    else:
        try:
            user_value = float(user_input)
            correct_value = float(st.session_state.answer)
            if abs(user_value - correct_value) < 1e-2:
                st.success("정답입니다! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"틀렸습니다. 정답은 {st.session_state.answer} 입니다.")
        except ValueError:
            st.warning("숫자를 입력해주세요.")

st.write(f"현재 점수: {st.session_state.score} 점")
