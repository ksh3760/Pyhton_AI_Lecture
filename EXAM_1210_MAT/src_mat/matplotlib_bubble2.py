# --------------------------------------------------------------------
# 데이터 시각화
# --------------------------------------------------------------------
# 모듈 로딩 -----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt


# 데이터 준비 --------------------------------------------------------
df = pd.read_csv('../data/auto-mpg.csv', header=None)

# 데이터 사전처리 -----------------------------------------------------
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터 가공 ---------------------------------------------------
# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성
cylinders_size = df.cylinders / df.cylinders.max() * 300

# 데이터 시각화 -----------------------------------------------------
# 3개의 변수로 산점도 그리기 
df.plot(kind='scatter', x='weight', y='mpg', marker='+', figsize=(10, 5),
        cmap='viridis', c=cylinders_size, s=50, alpha=0.3)
plt.title('Scatter Plot: mpg-weight-cylinders')

plt.savefig("./scatter.png")   
plt.savefig("./scatter_transparent.png", transparent=True)   

plt.show()