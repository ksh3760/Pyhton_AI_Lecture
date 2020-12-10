# --------------------------------------------------------------------
# 데이터 정보 확인
# --------------------------------------------------------------------
# 모듈 로딩 -----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt


# 데이터 준비 ---------------------------------------------------------
# excel => DataFrame 형태
df = pd.read_excel('../data/남북한발전전력량.xlsx')  # 데이터프레임 변환


# 데이터 가공 --------------------------------------------------------
df_ns = df.iloc[[5], 2:]            # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['North']        # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경

# 데이터 구조 & 정보 확인----------------------------------------------
# x축 ==> 년도 , y축 ==> 발전량 데이터
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
print(tdf_ns.info())
print('\n')
print(tdf_ns['North'].describe())
print('\n')
print('Min = {}, Max ={}'.format(tdf_ns['North'].min(), tdf_ns['North'].max()))
print('\n')

# 그래프 처리------------------------------------------------------
# 행, 열 전치하여 히스토그램 그리기
# 데이터를 지정된 구간(bins)로 나누어 표시
tdf_ns.plot(kind='hist', bins=5)
#tdf_ns.plot.hist(bins=5)
plt.show()