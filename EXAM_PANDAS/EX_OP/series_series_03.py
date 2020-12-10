# --------------------------------------------------
# Series & Series 사이 산술연산 메서드 사용
# --------------------------------------------------
# 모듈 로딩 -----------------------------------------
import pandas as pd
from EXAM_PANDAS.util import *

DEBUG=True

# 데이터 준비 -------------------------------------
# 국어, 영어, 수학, 과학 점수 데이터를 Series객체 저장
jumsu1=pd.Series({'국어':100, '영어':87, '수학':98, '과학':67})
jumsu2=pd.Series({'수학':80,  '과학':90})

# 생성된 데이터 확인 -------------------------------
if DEBUG:
    displaySInfo("jumsu1", jumsu1)
    displaySInfo("jumsu2", jumsu2)

# Series 객체 끼리 산술 연산 수행 ------------------
# 형식 : 시리즈객체변수명 연산자 숫자
sr_add=jumsu1.add(jumsu2, fill_value=0)
sr_sub=jumsu1.sub(jumsu2, fill_value=0)
sr_mul=jumsu1.mul(jumsu2, fill_value=0)
sr_div=jumsu1.div(jumsu2, fill_value=0)

print(f"sr_add==>\n{sr_add}\n\nsr_sub==>\n{sr_sub}\n")
print(f"sr_mul==>\n{sr_mul}\n\nsr_div==>\n{sr_div}\n")
