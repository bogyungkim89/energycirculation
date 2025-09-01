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
    <div style="width: 1200px; height: 600px; display: flex; flex-direction: column;">
        <div style="flex: 1; background-color: #302C44; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px; color: white; position: relative;">
            우주
            <div style="position: absolute; left: calc(50% - 15%); top: 0; transform: translateX(-50%); height: 100%; display: flex; flex-direction: column; align-items: center;">
                <div style="width: 160px; height: 120px; background-color: yellow; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                    <span style="font-size: 24px; font-weight: bold; color: #302C44;">태양복사</span>
                    <span style="font-size: 20px; color: #302C44;">100</span>
                </div>
                <div style="width: 0; height: 0; border-left: 140px solid transparent; border-right: 140px solid transparent; border-top: 70px solid yellow; margin-top: -10px;"></div>
            </div>
        </div>
        <div style="flex: 1.4; background-color: #CEEBF0; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px;">
            대기
        </div>
        <div style="height: 100px; background-color: #ABC53C; display: flex; justify-content: flex-start; align-items: center; font-size: 21px; padding-left: 20px;">
            지표
        </div>
    </div>
</div>
"""
st.components.v1.html(html_code, height=600)
