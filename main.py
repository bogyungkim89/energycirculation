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
    <div style="width: 1200px; height: 600px; border: 2px solid black; display: flex; flex-direction: column;">
        <div style="flex: 1; background-color: #f0f8ff; border-bottom: 2px solid black; display: flex; justify-content: center; align-items: center; font-size: 30px;">
            상단 영역
        </div>
        <div style="flex: 1; background-color: #f5fffa; border-bottom: 2px solid black; display: flex; justify-content: center; align-items: center; font-size: 30px;">
            중간 영역
        </div>
        <div style="flex: 1; background-color: #fff0f5; display: flex; justify-content: center; align-items: center; font-size: 30px;">
            하단 영역
        </div>
    </div>
</div>
"""
st.components.v1.html(html_code, height=600)
