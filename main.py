import streamlit as st
import numpy as np

# Streamlit 앱 제목 설정
st.title('지구 복사에너지 시뮬레이션')
st.write('지구의 반사율(Albedo)과 온실 효과를 조절하여 지구의 평형 온도가 어떻게 변하는지 확인해 보세요.')

# 사용자 입력 위젯
albedo = st.slider('지구의 반사율 (Albedo, α)', 0.0, 1.0, 0.3, 0.01)
transmissivity = st.slider('대기 투과율 (Greenhouse Effect, τ)', 0.0, 1.0, 0.61, 0.01)

# 상수 정의
S0 = 1368 # 태양복사량 W/m^2
sigma = 5.67e-8 # 슈테판-볼츠만 상수 W/m^2/K^4

# 평형 온도 계산 함수
def calculate_equilibrium_temp(albedo, transmissivity):
    absorbed_solar = S0 * (1 - albedo) / 4
    if transmissivity == 0:
        return 0
    temp_kelvin = (absorbed_solar / (transmissivity * sigma))**(1/4)
    temp_celsius = temp_kelvin - 273.15
    return temp_celsius

# 온도 계산 및 표시
temp_celsius = calculate_equilibrium_temp(albedo, transmissivity)
st.metric(label="지구의 평형 온도", value=f"{temp_celsius:.2f} °C")

# 추가 설명 및 시각화 (예시)
st.markdown("---")
st.subheader("모델 변수 설명")
st.write(f"**반사율 (Albedo)**: 빙하가 녹으면 반사율이 낮아져 흡수하는 에너지가 많아집니다.")
st.write(f"**대기 투과율 (Greenhouse Effect)**: 온실가스가 많아지면 투과율이 낮아져 열이 더 많이 갇히게 됩니다.")
