# --------------------------------------------------------------------
# 산점도 (Scatter Plot) - 값의 분포
# 열(column, 변수, 특징...)의 상관관계 시각화
# --------------------------------------------------------------------
# 모듈 로딩 -----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
# 데이터 준비 ---------------------------------------------------------
# csv => DataFrame 형태
df = pd.read_csv('../data/auto-mpg.csv', header=None)
# 데이터 사전처리 ------------------------------------------------------
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
# 그래프 ---------------------------------------------------------------
# 2개의 열을 선택하여 산점도 그리기
df.plot(x='weight',y='mpg', kind='scatter')
#df.plot.scatter(x='weight',y='mpg', s=14, c='Blue')
plt.show()