# ---------------------------------------------------
# JSON >> DataFrame 객체로 변환
# ---------------------------------------------------
# 라이브러리 로딩 -------------------------------------
import pandas as pd
from EXAM_PANDAS.util import  displayData, displayInfo

# 전역변수 선언 -----------------------------------------
file_path = '../data/sample.json'

# read_json() 함수로 데이터프레임 변환 
df1 = pd.read_json(file_path)
displayData('df1', df1)
