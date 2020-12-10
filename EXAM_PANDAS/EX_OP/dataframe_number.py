# ----------------------------------------------------
# DataFrame & Number 산술연산 수행
# ----------------------------------------------------
# 모듈로딩 --------------------------------------------
import pandas as pd
from EXAM_PANDAS.util import *

# 전역변수 --------------------------------------------
DEBUG=True

# 데이터 준비 -----------------------------------------
jumsu={ '이름' : ['학생1','학생2','학생3'],
        '수학' : [ 90, 80, 70],
        '영어' : [ 98, 89, 95],
        '음악' : [ 85, 95, 100],
        '체육' : [ 100, 90, 90]}

# 데이터 객체 생성 및 정보 확인 --------------------------
df=pd.DataFrame(jumsu)
# '이름' 컬럼을 인덱스로 설정
df.set_index('이름', inplace=True)
#df.reset_index(inplace=True)
if DEBUG:
    displayInfo('df', df)
    displayData('df', df)
    print(f"df.index.name => {df.index.name}")


# 산술 연산자로 연산 수행 --------------------------------
add10=df+10
sub10=df-10
mult2=df*2
div100=df/100

print(f"add10==>\n{add10}\n\nsub10==>\n{sub10}\n")
print(f"mult2==>\n{mult2}\n\ndiv100==>\n{div100}\n")
print(f"type(add10)={type(add10)} type(sub10)={type(sub10)}")
print(f"type(mult2)={type(mult2)} type(div100)={type(div100)}")

