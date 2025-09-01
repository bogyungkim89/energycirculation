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
    @keyframes drawArrow {
        0% {
            stroke-dasharray: 0 1000;
            opacity: 0;
        }
        50% {
            stroke-dasharray: 1000 0;
            opacity: 1;
        }
        100% {
            stroke-dasharray: 1000 0;
            opacity: 1;
        }
    }
    .animated-arrow {
        animation: drawArrow 3s ease-out forwards;
        animation-delay: 1s;
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
                  d="M 600 0 L 533.4 178.5"
                  stroke="yellow"
                  stroke-width="180"
                  stroke-linecap="butt"
                  marker-end="url(#arrowhead)"
                  fill="none" />

            <defs>
                <marker id="arrowhead" markerWidth="36" markerHeight="36" refX="18" refY="18" orient="auto">
                    <path d="M 0 0 L 36 18 L 0 36 z" fill="yellow" />
                </marker>
            </defs>
        </svg>
    </div>
</div>
"""
st.components.v1.html(html_code, height=600)
