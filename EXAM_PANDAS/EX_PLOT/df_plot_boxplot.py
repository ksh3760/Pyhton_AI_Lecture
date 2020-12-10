# --------------------------------------------------------------------
# 데이터 정보 확인
# --------------------------------------------------------------------
# 모듈 로딩 -----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt


# 데이터 준비 ---------------------------------------------------------
# csv => DataFrame 형태
df = pd.read_csv('../data/auto-mpg.csv', header=None)


# 데이터 가공 --------------------------------------------------------
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df[['mpg','cylinders']].describe())

# 그래프 처리------------------------------------------------------
# 열을 선택하여 박스 플롯 그리기
df[['mpg','cylinders']].plot(kind='box')
plt.show()