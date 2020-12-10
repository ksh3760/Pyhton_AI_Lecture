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

jumsu2={ '이름' : ['학생1','학생2'],
         '수학' : [ 90, 80],
         '영어' : [ 98, 89],
         '음악' : [ 85, 95],
         '체육' : [ 100, 90]}

# 데이터 객체 생성 및 정보 확인 --------------------------
df=pd.DataFrame(jumsu)
df.set_index('이름', inplace=True)

df2=pd.DataFrame(jumsu2)
df2.set_index('이름', inplace=True)

if DEBUG:
    displayData('df', df)
    displayData('df2', df2)


# DataFrame 산술 메서드로 연산 수행 --------------------------------
df_add=df.add(df2, fill_value=0)
df_sub=df.sub(df2, fill_value=0)
df_mul=df.mul(df2, fill_value=0)
df_div=df.div(df2, fill_value=0)

if 1:
    print(f"df_add==>\n{df_add}\n\ndf_sub==>\n{df_sub}\n")
    print(f"df_mul==>\n{df_mul}\n\ndf_div==>\n{df_div}\n")