# ==================================================================
# 인덱스 재생성
# df객체변수명.reindex( [새로운 인덱스] )
# ==================================================================
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

# 인덱스 재생성 후 지정 1---------------------------------
ndf = df.reindex(['r0', 'r1', 'r2', 'r3', 'r4'])
displayInfo("ndf", ndf)
displayData("ndf", ndf)

# 인덱스 재생성 후 지정 2---------------------------------
ndf2 = df.reindex(['A', 'B', 'C', 'r3', 'r4'])
displayInfo("ndf2", ndf2)
displayData("ndf2", ndf2)

# 인덱스 재생성 후 지정 3---------------------------------
ndf3 = df.reindex(['A', 'B', 'C', 'r3', 'r4'], fill_value=0)    # 비어있는 곳을 0으로 한다.
displayInfo("ndf3", ndf3)
displayData("ndf3", ndf3)

