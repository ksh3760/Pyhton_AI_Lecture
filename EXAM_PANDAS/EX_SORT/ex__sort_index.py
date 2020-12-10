# ----------------------------------------------------------
# 행 인덱스기반 정렬
# df.sort_index(ascending = True)
# 오름차순 정렬 => 0, 1, 2, 3,...     ascending = True
# 내림차순 정렬 => 9, 8, 7, 6,...     descending = False
# ----------------------------------------------------------
import pandas as pd
from EXAM_PANDAS.util import displayData, displayInfo

DEBUG = True

# 데이터 준비 --------------------------------------------------
dict_data = {'c0': [1, 2, 3],
             'c1': [4, 5, 6],
             'c2': [7, 8, 9],
             'c3': [10, 11, 12],
             'c4': [13, 14, 15]}

# 데이터 객체 생성 ----------------------------------------------
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
#if DEBUG: displayInfo()

# 내림차순으로 행 인덱스 정렬 --------------------------------------
ndf = df.sort_index(ascending=False)    # 내림차순
print("decending sort =>\n{}\n".format(ndf))

# 오름차순으로 행 인덱스 정렬
ndf = df.sort_index()                   # 기본값 오름차순
print("ascending sort =>\n{}\n".format(ndf))
