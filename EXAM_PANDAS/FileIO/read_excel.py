# ---------------------------------------------------
# EXCEL >> DataFrame 객체로 변환
# ---------------------------------------------------
# 라이브러리 로딩 -------------------------------------
import pandas as pd
from EXAM_PANDAS.util import  displayData, displayInfo


# 전역변수 선언 -----------------------------------------
file_path = '../data/남북한발전전력량.xlsx'

# read_excel() 함수로 데이터프레임 변환 
df1 = pd.read_excel(file_path)               # header=0 (default 옵션)
df2 = pd.read_excel(file_path, header=None)  # header=None 옵션

# 데이터프레임 출력
displayData("df1",df1)
df1.info()

displayData("df2 [header=None] ",df2)
df2.info()