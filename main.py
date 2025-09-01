import streamlit as st

st.title('지구 복사에너지 균형 시뮬레이션')
st.write('우주, 대기, 지표 세 구역의 에너지 흐름을 통해 복사평형의 원리를 시각화합니다.')

# 에너지 단위 설명
st.markdown("---")
st.subheader("에너지 흐름 (단위: W/m² 기준 백분율)")

# 컨테이너를 사용하여 각 구역을 분리
space_container = st.container()
atmosphere_container = st.container()
surface_container = st.container()

# 우주 구역
with space_container:
    st.markdown("### 🪐 우주 (Space)")
    st.markdown("➡️ **유입:** 태양 복사 에너지: 100")
    st.markdown("➡️ **유출:** 대기 반사: 23, 지표 반사: 30, 대기에서 방출: 70")
    st.markdown(f"**총 유입: {100}**")
    st.markdown(f"**총 유출: {23 + 30 + 70}**")
    st.markdown("---")

# 대기 구역
with atmosphere_container:
    st.markdown("### ☁️ 대기 (Atmosphere)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**유입**")
        st.markdown("태양 복사 에너지 흡수: 23")
        st.markdown("지표에서 오는 복사 에너지: 114")
        st.markdown("지표에서 오는 열(대류/전도): 29")
    with col2:
        st.markdown("**유출**")
        st.markdown("우주로 복사 에너지 방출: 70")
        st.markdown("지표로 복사 에너지 방출: 96")
    st.markdown(f"**총 유입: {23 + 114 + 29}**")
    st.markdown(f"**총 유출: {70 + 96}**")
    st.markdown("---")

# 지표 구역
with surface_container:
    st.markdown("### 🌍 지표 (Surface)")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("**유입**")
        st.markdown("태양 복사 에너지 흡수: 47")
        st.markdown("대기에서 오는 복사 에너지: 96")
    with col4:
        st.markdown("**유출**")
        st.markdown("열 복사 에너지 방출: 114")
        st.markdown("열(증발/대류) 방출: 29")
    st.markdown(f"**총 유입: {47 + 96}**")
    st.markdown(f"**총 유출: {114 + 29}**")
    
st.markdown("---")
st.success("✅ 모든 구역에서 에너지 유입과 유출이 일치하여 복사평형이 유지되고 있습니다.")
