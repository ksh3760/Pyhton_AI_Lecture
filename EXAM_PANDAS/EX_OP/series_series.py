# --------------------------------------------------
# Series & Series 사이 산술연산 수행
# --------------------------------------------------
# 모듈 로딩 -----------------------------------------
import pandas as pd
from EXAM_PANDAS.util import *

DEBUG=True

# 데이터 준비 -------------------------------------
# 국어, 영어, 수학, 과학 점수 데이터를 Series객체 저장
jumsu1=pd.Series({'국어':100, '영어':87, '수학':98, '과학':67})
jumsu2=pd.Series({'수학':80,  '과학':90, '영어':90, '국어':83})

# 생성된 데이터 확인 -------------------------------
if DEBUG:
    displaySInfo("jumsu1", jumsu1)
    displaySInfo("jumsu2", jumsu2)

# Series 객체 끼리 산술 연산 수행 ------------------
# 형식 : 시리즈객체변수명 연산자 숫자
add=jumsu1+jumsu2
sub=jumsu1-jumsu2
mul=jumsu1*jumsu2
div=jumsu1/jumsu2

print(f"add10==>\n{add}\n\nsub10==>\n{sub}\n")
print(f"mult2==>\n{mul}\n\ndiv100==>\n{div}\n")
print(f"type(add10)={type(add)} type(sub10)={type(sub)}")
print(f"type(mult2)={type(mul)} type(div100)={type(div)}")
