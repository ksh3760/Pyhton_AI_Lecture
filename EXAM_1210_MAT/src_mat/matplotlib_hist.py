# --------------------------------------------------------------------
# 데이터 시각화
# --------------------------------------------------------------------
# 모듈 로딩 -----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt


# 데이터 준비 ---------------------------------------------------------
df = pd.read_csv('../data/auto-mpg.csv', header=None)


# 데이터 사전처리 ------------------------------------------------------
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']


# 데이터 시각화 -----------------------------------------------------
# 연비(mpg) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))

plt.style.use('classic')   # 스타일 서식 지정

# 그래프 꾸미기
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()