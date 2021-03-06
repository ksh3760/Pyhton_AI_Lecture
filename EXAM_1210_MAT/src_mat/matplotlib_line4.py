# --------------------------------------------------------------------
# 데이터 시각화 & 한글 처리
# --------------------------------------------------------------------
# 모듈 로딩 -----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc     # matplotlib 한글 폰트 오류 문제 해결

# 데이터 준비 ---------------------------------------------------------
# Excel 데이터를 데이터프레임 변환
df = pd.read_excel('../data/시도별 전출입 인구수.xlsx', header=0)


# 데이터 사전처리-----------------------------------------------------
# (1) 한글 폰트 설정
font_path = "../data/malgun.ttf"   #폰트파일의 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# (2) 전출지별에서 누락값(NaN)을 앞 데이터로 채움 (엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

# (3) 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']


# 데이터 시각화 -----------------------------------------------------
# 스타일 서식 지정
plt.style.use('ggplot') 

# 그림 사이즈 지정
plt.figure(figsize=(14, 5))

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation='vertical')

# x, y축 데이터를 plot 함수에 입력 
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)  # 마커 표시 추가

plt.title('서울 -> 경기 인구 이동', size=30)  #차트 제목
plt.xlabel('기간', size=20)                  #x축 이름
plt.ylabel('이동 인구수', size=20)           #y축 이름

plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)   #범례 표시

plt.show()  # 변경사항 저장하고 그래프 출력
