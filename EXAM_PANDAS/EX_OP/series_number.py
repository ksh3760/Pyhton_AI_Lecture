# ------------------------------------------------
# Series & Number 산술 연산 실습
# ------------------------------------------------
# 모듈 로딩 ---------------------------------------
import pandas as pd
from EXAM_PANDAS.util import *

DEBUG=True

# 데이터 준비 -------------------------------------
# 국어, 영어, 수학, 과학 점수 데이터를 Series객체 저장
jumsu=pd.Series({'국어':100, '영어':87, '수학':98, '과학':67})

# 생성된 데이터 확인 -------------------------------
if DEBUG:
    displaySInfo("jumsu", jumsu)

# 산술연산 수행 -----------------------------------
# 형식 : 시리즈객체변수명 연산자 숫자
add10=jumsu+10
sub10=jumsu-10
mult2=jumsu*2
div100=jumsu/100

print(f"add10==>\n{add10}\n\nsub10==>\n{sub10}\n")
print(f"mult2==>\n{mult2}\n\ndiv100==>\n{div100}\n")
print(f"type(add10)={type(add10)} type(sub10)={type(sub10)}")
print(f"type(mult2)={type(mult2)} type(div100)={type(div100)}")

# 산술연산 결과를 DataFrame으로 저장 -----------------
opDf=pd.DataFrame([add10, sub10, mult2, div100],
                  index=["ADD", "SUB", "MUL", "DIV"])
# 생성된 DataFrame 확인
displayData("opDf", opDf)
