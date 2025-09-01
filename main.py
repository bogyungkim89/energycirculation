import streamlit as st

# 웹 앱 제목 설정
st.title("☀️ 지구 복사 에너지 시뮬레이션")

st.set_page_config(layout="wide")

# CSS를 사용하여 레이아웃 스타일링
st.markdown("""
<style>
    .simulation-box {
        width: 800px; /* 가로 800px */
        height: 400px; /* 세로 400px (2:1 비율) */
        border: 2px solid #333;
        display: block;
        margin: auto; /* 상자를 중앙에 배치 */
        display: flex;
        flex-direction: column;
    }
    .space, .atmosphere, .surface {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        font-weight: bold;
        color: white;
        text-shadow: 1px 1px 2px black;
        text-align: center;
    }
    .space {
        background-color: #000033; /* 짙은 남색 */
        flex: 1; /* 높이 비율 1 */
    }
    .atmosphere {
        background-color: #87CEEB; /* 하늘색 */
        flex: 1; /* 높이 비율 1 */
    }
    .surface {
        background-color: #228B22; /* 짙은 초록색 */
        flex: 1; /* 높이 비율 1 */
    }
</style>
""", unsafe_allow_html=True)

# 시뮬레이션 상자
st.markdown('<div class="simulation-box">', unsafe_allow_html=True)

# 우주 (시뮬레이션 상자 내부)
st.markdown('<div class="space">우주</div>', unsafe_allow_html=True)

# 대기 (시뮬레이션 상자 내부)
st.markdown('<div class="atmosphere">대기</div>', unsafe_allow_html=True)

# 지표 (시뮬레이션 상자 내부)
st.markdown('<div class="surface">지표</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
