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
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off') # 축 숨기기

    # 구역 정의 (사각형)
    # y축: 0-1 지표, 1-2 대기, 2-3 우주 (역순으로 그리기)
    surface_rect = patches.Rectangle((0, 0), 2, 1, linewidth=2, edgecolor='brown', facecolor='lightgreen', alpha=0.6, label='지표')
    atmosphere_rect = patches.Rectangle((0, 1), 2, 1, linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.6, label='대기')
    space_rect = patches.Rectangle((0, 2), 2, 1, linewidth=2, edgecolor='gray', facecolor='lightgray', alpha=0.6, label='우주')

    ax.add_patch(surface_rect)
    ax.add_patch(atmosphere_rect)
    ax.add_patch(space_rect)

    # 구역 텍스트 추가
    ax.text(1, 0.5, '지표', ha='center', va='center', fontsize=14, fontweight='bold', color='darkgreen')
    ax.text(1, 1.5, '대기', ha='center', va='center', fontsize=14, fontweight='bold', color='darkblue')
    ax.text(1, 2.5, '우주', ha='center', va='center', fontsize=14, fontweight='bold', color='dimgray')

    # 화살표 그리기 (FancyArrowPatch 사용)
    # 화살표 두께는 에너지 값에 비례
    # 화살표 시작점과 끝점 조정 (겹치지 않도록)
    
    # 우주 -> 대기 (태양 복사)
    ax.annotate(f"{flows['Solar_to_Atmosphere']}", xy=(0.7, 1.9), xytext=(0.7, 2.1),
                arrowprops=dict(facecolor='orange', shrink=0.05, width=flows['Solar_to_Atmosphere']/10, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='bottom', color='darkorange', fontsize=12)
    ax.text(0.7, 2.2, f"태양 복사", ha='center', va='bottom', fontsize=10, color='darkorange')

    # 우주 -> 지표 (태양 복사)
    ax.annotate(f"{flows['Solar_to_Surface']}", xy=(1.3, 0.9), xytext=(1.3, 2.1),
                arrowprops=dict(facecolor='orange', shrink=0.05, width=flows['Solar_to_Surface']/10, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='bottom', color='darkorange', fontsize=12)
    ax.text(1.3, 2.2, f"태양 복사", ha='center', va='bottom', fontsize=10, color='darkorange')

    # 대기 -> 우주 (대기 반사)
    ax.annotate(f"{flows['Atmosphere_Reflect_to_Space']}", xy=(0.2, 2.1), xytext=(0.2, 1.9),
                arrowprops=dict(facecolor='lightblue', shrink=0.05, width=flows['Atmosphere_Reflect_to_Space']/10, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='top', color='darkblue', fontsize=12)
    ax.text(0.2, 1.8, f"대기 반사", ha='center', va='top', fontsize=10, color='darkblue')
    
    # 지표 -> 우주 (지표 반사)
    ax.annotate(f"{flows['Surface_Reflect_to_Space']}", xy=(1.8, 2.1), xytext=(1.8, 0.9),
                arrowprops=dict(facecolor='lightgreen', shrink=0.05, width=flows['Surface_Reflect_to_Space']/10, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='top', color='darkgreen', fontsize=12)
    ax.text(1.8, 0.8, f"지표 반사", ha='center', va='top', fontsize=10, color='darkgreen')

    # 대기 -> 우주 (대기 방출)
    ax.annotate(f"{flows['Atmosphere_Emits_to_Space']}", xy=(0.5, 2.1), xytext=(0.5, 1.9),
                arrowprops=dict(facecolor='red', shrink=0.05, width=flows['Atmosphere_Emits_to_Space']/10, headwidth=10, headlength=10),
                horizontalalignment='center', verticalalignment='top', color='darkred', fontsize=12)
    ax.text(0.5, 1.8, f"대기 방출", ha='center', va='top', fontsize=10, color='darkred')

    # 지표 -> 대기 (지표 복사)
    ax.annotate(f
