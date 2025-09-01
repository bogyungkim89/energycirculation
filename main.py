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
<div style="display: flex; justify-content: center; align-items: center; width: 100%;">
    <div style="width: 1200px; height: 600px; display: flex; flex-direction: column; position: relative; overflow: hidden;">
        <div style="flex: 1; background-color: #302C44; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px; color: white; position: relative; z-index: 1;">
            우주
            <div style="position: absolute; left: calc(50% - 15% + 2% + 2px); top: -7px; transform: translateX(-50%); height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div style="width: 160px; height: 120px; background-color: yellow; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                    <span style="font-size: 24px; font-weight: bold; color: #302C44;">태양복사</span>
                    <span style="font-size: 20px; color: #302C44;">100</span>
                </div>
                <div id="yellow-arrowhead" style="width: 0; height: 0; border-left: 140px solid transparent; border-right: 140px solid transparent; border-top: 70px solid yellow; margin-top: -10px;"></div>
            </div>
        </div>
        <div style="flex: 1.4; background-color: #CEEBF0; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px; color: #302C44; position: relative; z-index: 1;">
            대기
        </div>
        <div style="height: 100px; background-color: #ABC53C; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px; color: #302C44; position: relative; z-index: 1;">
            지표
        </div>

        <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 2;">
            <defs>
                <marker id="u-arrowhead" markerWidth="4" markerHeight="2" refX="1" refY="1" orient="auto">
                    <path d="M 0 0 L 2 1 L 0 2 z" fill="blue" />
                </marker>
                 <marker id="o-arrowhead" markerWidth="4" markerHeight="2" refX="1" refY="1" orient="auto">
                    <path d="M 0 0 L 2 1 L 0 2 z" fill="orange" />
                </marker>
                <marker id="u-arrowhead-large" markerWidth="6.8" markerHeight="3.4" refX="1" refY="1" orient="auto">
                    <path d="M 0 0 L 2 1 L 0 2 z" fill="blue" />
                </marker>
            </defs>
            <path d="M 420 188.33 L 420 280 C 420 310, 390 330, 336 330 C 282 330, 252 310, 252 280 L 252 100" stroke="blue" stroke-width="40" fill="none" marker-end="url(#u-arrowhead)" />
            <text x="252" y="25.3" font-family="Arial" font-size="20" fill="white" text-anchor="middle" font-weight="bold">대기반사</text>
            <text x="252" y="50.3" font-family="Arial" font-size="20" fill="white" text-anchor="middle" font-weight="bold">25</text>
            <path d="M 432 253.8 L 432 433.8 C 432 463.8, 381.8 493.8, 280.2 493.8 C 178.6 493.8, 128.4 463.8, 128.4 433.8 L 128.4 75.3" stroke="blue" stroke-width="13.33" fill="none" marker-end="url(#u-arrowhead-large)" />
            <text x="128.4" y="25.3" font-family="Arial" font-size="20" fill="white" text-anchor="middle" font-weight="bold">지표반사</text>
            <text x="128.4" y="50.3" font-family="Arial" font-size="20" fill="white" text-anchor="middle" font-weight="bold">5</text>
            <path d="M 518 188.33 L 518 500" stroke="orange" stroke-width="64" fill="none" marker-end="url(#o-arrowhead)" />
            <path d="M 614 188.33 L 614 500" stroke="orange" stroke-width="32" fill="none" marker-end="url(#o-arrowhead)" />
        </svg>
    </div>
</div>
"""
st.components.v1.html(html_code, height=600)
