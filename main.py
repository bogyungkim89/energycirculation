import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(layout="wide") # 넓은 레이아웃 사용

st.title('지구 복사에너지 균형 시뮬레이션')
st.write('우주, 대기, 지표 구역 간 에너지 흐름을 화살표 두께로 시각화합니다.')

# --- 에너지 흐름 데이터 정의 (단위: 상대적인 크기) ---
energy_flows = {
    # 우주 -> 지구 (태양 복사)
    "Solar_to_Atmosphere": 23,
    "Solar_to_Surface": 47,
    # 지구 -> 우주 (반사 및 방출)
    "Atmosphere_Reflect_to_Space": 23, # 태양 복사의 일부 대기 반사
    "Surface_Reflect_to_Space": 30, # 태양 복사의 일부 지표 반사
    "Atmosphere_Emits_to_Space": 70, # 대기가 우주로 방출
    # 지표 <-> 대기
    "Surface_Emits_to_Atmosphere": 114, # 지표가 대기로 열 방출 (적외선)
    "Atmosphere_Emits_to_Surface": 96, # 대기가 지표로 열 방출 (온실 효과)
    "Surface_Convection_to_Atmosphere": 29, # 지표에서 대기로 대류/증발
}

# --- 시각화 함수 ---
def plot_energy_flow(flows):
    # 전체 그림의 크기를 조정: 가로 1.7배, 세로 0.5배
    fig, ax = plt.subplots(figsize=(17, 4))
    
    # x축 범위 조정 (가로 1.7배)
    ax.set_xlim(-0.25, 3.65) # 기존 2 -> 3.4 이므로 여백 포함

    # y축 범위 조정 (높이 절반)
    # 각 사각형 높이 0.5, 총 3개 구역이므로 0.5 * 3 = 1.5
    ax.set_ylim(-0.25, 1.75) # 여백 포함하여 y 범위 설정

    ax.set_aspect('equal')
    ax.axis('off') # 축 숨기기

    # 구역 정의 (사각형) - 높이 0.5, 너비 3.4로 조정
    surface_height = 0.5
    box_width = 3.4

    # y축: 0-0.5 지표, 0.5-1.0 대기, 1.0-1.5 우주
    surface_rect = patches.Rectangle((0, 0), box_width, surface_height, linewidth=2, edgecolor='brown', facecolor='lightgreen', alpha=0.6, label='지표')
    atmosphere_rect = patches.Rectangle((0, surface_height), box_width, surface_height, linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.6, label='대기')
    space_rect = patches.Rectangle((0, surface_height * 2), box_width, surface_height, linewidth=2, edgecolor='gray', facecolor='lightgray', alpha=0.6, label='우주')

    ax.add_patch(surface_rect)
    ax.add_patch(atmosphere_rect)
    ax.add_patch(space_rect)

    # 구역 텍스트 추가 (y 좌표 조정)
    ax.text(box_width / 2, surface_height / 2, '지표', ha='center', va='center', fontsize=14, fontweight='bold', color='darkgreen')
    ax.text(box_width / 2, surface_height * 1.5, '대기', ha='center', va='center', fontsize=14, fontweight='bold', color='darkblue')
    ax.text(box_width / 2, surface_height * 2.5, '우주', ha='center', va='center', fontsize=14, fontweight='bold', color='dimgray')

    # 화살표 그리기 (FancyArrowPatch 사용)
    # 화살표 두께는 에너지 값에 비례
    # 화살표 시작점과 끝점 조정 (겹치지 않도록, y 좌표 조정)
    
    # 우주 -> 대기 (태양 복사)
    ax.annotate(f"{flows['Solar_to_Atmosphere']}", xy=(box_width * 0.25, surface_height * 2 + 0.05), xytext=(box_width * 0.25, surface_height * 2.45), # xy는 화살표 끝, xytext는 화살표 시작점
                arrowprops=dict(facecolor='orange', shrink=0.05, width=flows['Solar_to_Atmosphere']/15, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='bottom', color='darkorange', fontsize=12)
    # ax.text(box_width * 0.25, surface_height * 2.6, f"태양 복사", ha='center', va='bottom', fontsize=10, color='darkorange') # 삭제

    # 우주 -> 지표 (태양 복사)
    ax.annotate(f"{flows['Solar_to_Surface']}", xy=(box_width * 0.75, surface_height * 0.05), xytext=(box_width * 0.75, surface_height * 2.45),
                arrowprops=dict(facecolor='orange', shrink=0.05, width=flows['Solar_to_Surface']/15, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='bottom', color='darkorange', fontsize=12)
    # ax.text(box_width * 0.75, surface_height * 2.6, f"태양 복사", ha='center', va='bottom', fontsize=10, color='darkorange') # 삭제

    # 대기 -> 우주 (대기 반사)
    ax.annotate(f"{flows['Atmosphere_Reflect_to_Space']}", xy=(box_width * 0.1, surface_height * 2.45), xytext=(box_width * 0.1, surface_height * 2 + 0.05),
                arrowprops=dict(facecolor='lightblue', shrink=0.05, width=flows['Atmosphere_Reflect_to_Space']/15, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='top', color='darkblue', fontsize=12)
    # ax.text(box_width * 0.1, surface_height * 1.8, f"대기 반사", ha='center', va='top', fontsize=10, color='darkblue') # 삭제
    
    # 지표 -> 우주 (지표 반사)
    ax.annotate(f"{flows['Surface_Reflect_to_Space']}", xy=(box_width * 0.9, surface_height * 2.45), xytext=(box_width * 0.9, surface_height * 0.05),
                arrowprops=dict(facecolor='lightgreen', shrink=0.05, width=flows['Surface_Reflect_to_Space']/15, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='top', color='darkgreen', fontsize=12)
    # ax.text(box_width * 0.9, surface_height * 0.05 - 0.2, f"지표 반사", ha='center', va='top', fontsize=10, color='darkgreen') # 삭제

    # 대기 -> 우주 (대기 방출)
    ax.annotate(f"{flows['Atmosphere_Emits_to_Space']}", xy=(box_width * 0.4, surface_height * 2.45), xytext=(box_width * 0.4, surface_height * 2 + 0.05),
                arrowprops=dict(facecolor='red', shrink=0.05, width=flows['Atmosphere_Emits_to_Space']/15, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='top', color='darkred', fontsize=12)
    # ax.text(box_width * 0.4, surface_height * 1.8, f"대기 방출", ha='center', va='top', fontsize=10, color='darkred') # 삭제

    # 지표 -> 대기 (지표 복사)
    ax.annotate(f"{flows['Surface_Emits_to_Atmosphere']}", xy=(box_width * 0.2, surface_height + 0.05), xytext=(box_width * 0.2, surface_height - 0.05),
                arrowprops=dict(facecolor='red', shrink=0.05, width=flows['Surface_Emits_to_Atmosphere']/15, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='top', color='darkred', fontsize=12)
    # ax.text(box_width * 0.2, surface_height - 0.2, f"지표 복사", ha='center', va='top', fontsize=10, color='darkred') # 삭제

    # 대기 -> 지표 (대기 복사 - 온실 효과)
    ax.annotate(f"{flows['Atmosphere_Emits_to_Surface']}", xy=(box_width * 0.8, surface_height - 0.05), xytext=(box_width * 0.8, surface_height + 0.05),
                arrowprops=dict(facecolor='purple', shrink=0.05, width=flows['Atmosphere_Emits_to_Surface']/15, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='bottom', color='darkmagenta', fontsize=12)
    # ax.text(box_width * 0.8, surface_height + 0.2, f"대기 복사", ha='center', va='bottom', fontsize=10, color='darkmagenta') # 삭제

    # 지표 -> 대기 (대류/증발)
    ax.annotate(f"{flows['Surface_Convection_to_Atmosphere']}", xy=(box_width * 0.6, surface_height + 0.05), xytext=(box_width * 0.6, surface_height - 0.05),
                arrowprops=dict(facecolor='blue', shrink=0.05, width=flows['Surface_Convection_to_Atmosphere']/15, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='top', color='darkblue', fontsize=12)
    # ax.text(box_width * 0.6, surface_height - 0.2, f"대류/증발", ha='center', va='top', fontsize=10, color='darkblue') # 삭제

    st.pyplot(fig)

# 시각화 실행
plot_energy_flow(energy_flows)

st.markdown("---")
st.subheader("에너지 균형 요약")

# 각 구역별 에너지 합계 계산 및 표시
col_space, col_atm, col_surf = st.columns(3)

with col_space:
    st.markdown("### 🪐 우주")
    space_in = 100  # 전체 태양 복사량
    space_out = energy_flows["Atmosphere_Reflect_to_Space"] + energy_flows["Surface_Reflect_to_Space"] + energy_flows["Atmosphere_Emits_to_Space"]
    st.write(f"**유입**: 태양 복사 = {space_in}")
    st.write(f"**유출**: 반사 및 방출 = {space_out}")
    st.write(f"**총합**: {space_in - space_out} (W/m²)")

with col_atm:
    st.markdown("### ☁️ 대기")
    atm_in = energy_flows["Solar_to_Atmosphere"] + energy_flows["Surface_Emits_to_Atmosphere"] + energy_flows["Surface_Convection_to_Atmosphere"]
    atm_out = energy_flows["Atmosphere_Emits_to_Space"] + energy_flows["Atmosphere_Emits_to_Surface"]
    st.write(f"**유입**: 태양 흡수 ({energy_flows['Solar_to_Atmosphere']}), 지표 방출 ({energy_flows['Surface_Emits_to_Atmosphere']}), 대류/증발 ({energy_flows['Surface_Convection_to_Atmosphere']})")
    st.write(f"**총 유입**: {atm_in}")
    st.write(f"**유출**: 우주 방출 ({energy_flows['Atmosphere_Emits_to_Space']}), 지표 방출 ({energy_flows['Atmosphere_Emits_to_Surface']})")
    st.write(f"**총 유출**: {atm_out}")
    st.write(f"**총합**: {atm_in - atm_out} (W/m²)")

with col_surf:
    st.markdown("### 🌍 지표")
    surf_in = energy_flows["Solar_to_Surface"] + energy_flows["Atmosphere_Emits_to_Surface"]
    surf_out = energy_flows["Surface_Emits_to_Atmosphere"] + energy_flows["Surface_Convection_to_Atmosphere"]
    st.write(f"**유입**: 태양 흡수 ({energy_flows['Solar_to_Surface']}), 대기 방출 ({energy_flows['Atmosphere_Emits_to_Surface']})")
    st.write(f"**총 유입**: {surf_in}")
    st.write(f"**유출**: 대기 방출 ({energy_flows['Surface_Emits_to_Atmosphere']}), 대류/증발 ({energy_flows['Surface_Convection_to_Atmosphere']})")
    st.write(f"**총 유출**: {surf_out}")
    st.write(f"**총합**: {surf_in - surf_out} (W/m²)")

st.markdown("---")
st.success("✅ 위 시뮬레이션은 단순화된 모델이며, 모든 구역의 에너지 흐름이 이론적으로 균형을 이룹니다. 하지만 실제 지구 시스템에서는 미세한 차이가 발생할 수 있습니다.")
