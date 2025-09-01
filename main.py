import streamlit as st

st.set_page_config(layout="wide")

st.title("지구 열수지 알아보기")

html_code = """
<div style="display: flex; justify-content: center; align-items: center; width: 100%;">
    <div style="width: 600px; height: 300px; border: 2px solid black; display: flex;">
        <div style="flex: 1; background-color: #f0f8ff; border-right: 2px solid black; display: flex; justify-content: center; align-items: center; font-size: 20px;">
            영역 1
        </div>
        <div style="flex: 1; background-color: #f5fffa; border-right: 2px solid black; display: flex; justify-content: center; align-items: center; font-size: 20px;">
            영역 2
        </div>
        <div style="flex: 1; background-color: #fff0f5; display: flex; justify-content: center; align-items: center; font-size: 20px;">
            영역 3
        </div>
    </div>
</div>
"""
st.components.v1.html(html_code, height=300)
