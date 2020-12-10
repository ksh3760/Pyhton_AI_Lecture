# ---------------------------------------------------
# CSV -->> DataFrame 데이터 저장
# ---------------------------------------------------
# 라이브러리 로딩 -------------------------------------
import pandas as pd
from EXAM_PANDAS.util import *

# 전역변수 선언 -----------------------------------------
file_path = '../data/sample.csv'

# csv => DataFrame 객체 생성 ----------------------------
df1 = pd.read_csv(file_path)
displayData('df1', df1)

# header= 열 이름으로 사용할 행(Row)설정 ===================
# header=0  : 0번행을 열이름으로 지정 (기본값)
df2 = pd.read_csv(file_path, header=0)
displayData('df2 [ header=0 ]', df2)

# header=1  : 1번행을 열이름으로 지정
df3 = pd.read_csv(file_path, header=1)
displayData('df3 [ header=1 ]', df3)

# header=2 : 2번행을 열이름으로 지정
df4 = pd.read_csv(file_path, header=2)
displayData('df4 [ header=2 ]', df4)

# header=None : 행을 열이름으로 지정하지 않음
df4 = pd.read_csv(file_path, header=None)
displayData('df4 [ header=None ]', df4)

# index_col=행 인덱스로 사용할 열(컬럼) 설정 ---------------------------
# index_col=False 미지정
df5 = pd.read_csv(file_path, index_col=False)
displayData('df5 [ index_col=False ]', df5)

# index_col='c1' 옵션
df6 = pd.read_csv(file_path, index_col='c1')
displayData("df6 [ index_col='c1' ]", df6)

# 멀티 행 인덱스 설정
df7 = pd.read_csv(file_path, index_col=['c1','c3'])
displayData("df7 [ index_col=['c1','c3'] ]", df7)

df7.reset_index(inplace=True)
displayData("df7 reset_index(inplace=True)", df7)

# 몇 개의 행(row) 데이터에서 제외
df8=pd.read_csv(file_path, skiprows=2)
displayData("df8 [skiprows=2]", df8)

if 0:
    # header= 열 이름으로 사용할 행(Row) 설정

    # header=0  : 0번행을 열이름으로 지정 (기본값)
    df2 = pd.read_csv(file_path, header=0)
    displayData('df2 [ header=0 ]', df2)

    # header=1  : 1번행을 열이름으로 지정
    df2 = pd.read_csv(file_path, header=1)
    displayData('df2 [ header=1 ]', df2)

    # header=1  : 1번행을 열이름으로 지정
    df2 = pd.read_csv(file_path, header=1)
    displayData('df2 [ header=1 ]', df2)

    # header=None  : 행을 열이름으로 지정하지 않음
    df2 = pd.read_csv(file_path, header=None)
    displayData('df2 [ header=None ]', df2)

if 0:
    # index_col=행 인덱스로 사용할 열(컬럼) 설정
    # index_col=False 미지정
    df3 = pd.read_csv(file_path, index_col=False)
    displayData('df3 [ index_col=False ]', df3)

    # index_col='c0' 옵션
    df4 = pd.read_csv(file_path, index_col='c1')
    displayData("df4 [ index_col='c1' ]", df4)

    df4.reset_index(inplace=True)
    displayData("df4 [ df4.reset_index()]", df4)