import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import plotly.express as px
from pathlib import Path

font_path = Path(__file__).resolve().parents[1] / "fonts" / "NotoSansKR-Regular.ttf"
if font_path.exists():
    fm.fontManager.addfont(str(font_path))
    font_prop = fm.FontProperties(fname=str(font_path))
    font_name = font_prop.get_name()
    plt.rcParams["font.family"] = font_name
    plt.rcParams["font.sans-serif"] = [font_name]
    plt.rcParams["axes.unicode_minus"] = False
    sns.set(font=font_name)
else:
    st.warning("한글 폰트 파일을 찾을 수 없습니다. fonts/NotoSansKR-Regular.ttf 파일을 확인해주세요.")

st.title("📊 그래프 그리기 예제")
st.write("matplotlib, seaborn, plotly를 사용한 그래프 예시입니다. 모두 한글로 표시됩니다.")

# Matplotlib 예시
st.header("1. Matplotlib 막대 그래프")
mat_data = {
    "카테고리": ["사과", "바나나", "포도", "딸기", "오렌지"],
    "개수": [15, 22, 9, 18, 12],
}
mat_df = pd.DataFrame(mat_data)
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(mat_df["카테고리"], mat_df["개수"], color=["#f07167", "#f8bd96", "#a6dcef", "#ba9bff", "#ffd166"])
ax.set_title("과일 개수", fontsize=16)
ax.set_xlabel("과일 종류", fontsize=12)
ax.set_ylabel("수량", fontsize=12)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
for i, value in enumerate(mat_df["개수"]):
    ax.text(i, value + 0.5, str(value), ha="center", fontsize=11)
st.pyplot(fig)

st.markdown("---")

# Seaborn 예시
st.header("2. Seaborn 상자 그림")
sea_df = pd.DataFrame({
    "그룹": np.repeat(["A팀", "B팀", "C팀"], 20),
    "점수": np.concatenate([
        np.random.normal(loc=80, scale=6, size=20),
        np.random.normal(loc=72, scale=8, size=20),
        np.random.normal(loc=88, scale=5, size=20),
    ]),
})
fig2, ax2 = plt.subplots(figsize=(7, 4))
sns.boxplot(x="그룹", y="점수", data=sea_df, palette=["#66c2a5", "#fc8d62", "#8da0cb"], ax=ax2)
ax2.set_title("팀별 시험 점수 분포", fontsize=16)
ax2.set_xlabel("팀", fontsize=12)
ax2.set_ylabel("점수", fontsize=12)
st.pyplot(fig2)

st.markdown("---")

# Plotly 예시
st.header("3. Plotly 라인 그래프")
plotly_df = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "매출": [120, 150, 170, 160, 190, 220],
    "비용": [80, 90, 85, 95, 100, 110],
})
fig3 = px.line(
    plotly_df,
    x="월",
    y=["매출", "비용"],
    title="월별 매출과 비용",
    labels={"value": "금액(단위: 만원)", "variable": "항목"},
)
fig3.update_traces(mode="markers+lines")
fig3.update_layout(title_font_size=18, legend_title_text="구분", xaxis_title="월", yaxis_title="금액(만원)")
st.plotly_chart(fig3, use_container_width=True)
