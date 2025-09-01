import streamlit as st

st.set_page_config(layout="wide")

st.title("지구 열수지 알아보기")

html_code = """
<div style="display: flex; justify-content: center; align-items: center; width: 100%;">
    <div style="width: 600px; height: 300px; border: 2px solid black; display: flex; flex-direction: column;">
        <div style="flex: 1; background-color: #f0f8ff; border-bottom: 2px solid black; display: flex; justify-content: center; align-items: center; font-size: 20px;">
            상단 영역
        </div>
        <div style="flex: 1; background-color: #f5fffa; border-bottom: 2px solid black; display: flex; justify-content: center; align-items: center; font-size: 20px;">
            중간 영역
        </div>
        <div style="flex: 1; background-color: #fff0f5; display: flex; justify-content: center; align-items: center; font-size: 20px;">
            하단 영역
        </div>
    </div>
</div>
"""
st.components.v1.html(html_code, height=300)
