# 모듈 로딩 ------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager as fm   # 한글 폰트 설정

# Pandas로 CSV 데이터 파일 가져오기 -----------------------
tbl = pd.read_csv("../../DATA/BMI/bmi.csv", index_col=2)

# (2) 그래프 그리기 -----------------------------------------
# 한글 설정
font_path = r'C:\Windows\Fonts\malgun.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
print(font_name)
plt.rc('font', family=font_name)     # mpl.rcParams['font.family'] = 'Gullim'
plt.rc('axes', unicode_minus=False)  # mpl.rcParams['axes.unicode_minus'] = False

# 분포도 그래프 그리기
plt.scatter(tbl.loc['fat']["weight"],   tbl.loc['fat']["height"],      c='red',    label='fat')
plt.scatter(tbl.loc['normal']["weight"],tbl.loc['normal']["height"],   c='yellow', label='normal')
plt.scatter(tbl.loc['thin']["weight"],  tbl.loc['thin']["height"],     c='purple', label='thin')

# 범례, 라벨 출력 및 저장
plt.legend(loc='upper right')
plt.ylabel('키')
plt.xlabel('몸무게')
plt.savefig("../../DATA/BMI/bmi-test.png")
plt.show()