# ------------------------------------------------
# 데이터 프레임의 인덱스 설정
# 정수형(0, 1, 2, ...) 인덱스
# df 객체변수명.reset_index()
# ------------------------------------------------
import pandas as pd
import EXAM_PANDAS.util as util    # EXAM_PANDAS내의 util.py 파일을 import하여 util이라는 이름으로 사용
from EXAM_PANDAS.util import displayData, displayInfo

DEBUG = True

# 데이터 준비 ---------------------------------------
exam_data = {'수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

# 데이터 객체 생성 ------------------------------------
df = pd.DataFrame(exam_data, index=['A', 'B', 'C'])

# 개발 중 확인용(디버그용) ------------------------------
if DEBUG: displayInfo("df", df)

# 수학 열(컬럼)으로 인덱스 설정 -------------------------
ndf = df.set_index('수학')
if DEBUG:
    displayInfo("ndf", ndf)
    displayData("ndf", ndf)

# 0-base 인덱스로 재설정 ------------------------------------
rndf = ndf.reset_index()
if DEBUG:
    #displayInfo("rndf", rndf)
    displayData("rndf(Drop)", rndf)

rndf = ndf.reset_index(drop=True)
if DEBUG:
    displayInfo("rndf", rndf)
    displayData("rndf", rndf)

# 수학, 음악 열(칼럼)으로 인덱스 설정 --------------------------
ndf2 = df.set_index(['수학', '음악'])
if DEBUG:
    displayInfo("ndf2", ndf2)
    displayData("ndf2", ndf2)

# 0-base 인덱스로 재설정 ------------------------------------
rndf2 = ndf2.reset_index()
if DEBUG:
    displayInfo("rndf2", rndf2)
    displayData("rndf2", rndf2)

