import pandas as pd
import EXAM_PANDAS.util as util    # EXAM_PANDAS내의 util.py 파일을 import하여 util이라는 이름으로 사용
from EXAM_PANDAS.util import displayData, displayInfo

DEBUG = True

# 데이터 준비 ---------------------------------------
exam_data = {'이름': ['학생1', '학생2', '학생3', '학생4'],
             '수학': [90, 80, 70, 80],
             '영어': [98, 89, 95, 76],
             '음악': [85, 95, 100, 90],
             '체육': [100, 90, 90, 80]}

# 데이터 객체 생성 ------------------------------------
df = pd.DataFrame(exam_data, index=['r0', 'r1', 'r2', 'r3'])
if DEBUG: displayInfo("df", df)

# 특정 칼럼으로 정렬하기 -------------------------------
# 수학 컬럼으로 오름차순 정렬
mdf = df.sort_values(by='수학')
displayData('mdf', mdf)

# 수학 컬럼으로 내림차순 정렬
mdf = df.sort_values(by='수학', ascending=False)
displayData('mdf-DES', mdf)

# 수학, 음악 컬럼으로 오름차순 정렬
mmdf = df.sort_values(by=['수학', '음악'])
displayData("mmdf-AS", mmdf)

# 수학, 음악 컬럼으로 오름차순 정렬
mmdf = df.sort_values(by=['수학', '음악'], ascending=False)
displayData("mmdf-AS", mmdf)

