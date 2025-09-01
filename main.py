import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center;">
        <span style="font-size: 50px; margin-right: 10px;">🌞</span>
        <h1 style="text-align: center; display: inline-block; margin: 0;">지구 열수지 알아보기</h1>
        <span style="font-size: 50px; margin-left: 10px;">🌍</span>
    </div>
    """,
    unsafe_allow_html=True
)

html_code = """
<style>
    @keyframes extendArrow {
        0% {
            stroke-dasharray: 0 1000;
        }
        100% {
            stroke-dasharray: 1000 0;
        }
    }
    .animated-arrow {
        animation: extendArrow 3s ease-out forwards; /* 3초 동안 부드럽게 애니메이션 */
        animation-delay: 1s; /* 1초 후에 애니메이션 시작 */
    }
</style>

<div style="display: flex; justify-content: center; align-items: center; width: 100%; position: relative;">
    <div style="width: 1200px; height: 600px; display: flex; flex-direction: column; position: relative; overflow: hidden;">
        <div style="flex: 1; background-color: #302C44; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px; color: white; position: relative; z-index: 1;">
            우주
        </div>
        <div style="flex: 1.4; background-color: #CEEBF0; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px; position: relative; z-index: 1;">
            대기
        </div>
        <div style="height: 100px; background-color: #ABC53C; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px; position: relative; z-index: 1;">
            지표
        </div>

        <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 2;">
            <path class="animated-arrow"
                  d="M 600 0 L 526 198.33"
                  stroke="red"
                  stroke-width="20"
                  stroke-linecap="round"
                  marker-end="url(#arrowhead)"
                  fill="none" />

            <defs>
                <marker id="arrowhead" markerWidth="20" markerHeight="20" refX="10" refY="5" orient="auto">
                    <path d="M 0 0 L 10 5 L 0 10 z" fill="red" />
                </marker>
            </defs>
        </svg>
    </div>
</div>
"""
st.components.v1.html(html_code, height=600)
