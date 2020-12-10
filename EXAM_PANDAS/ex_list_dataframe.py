# ------------------------------------------
# list 데이터기반 DataFrame 생성
# ------------------------------------------
# 모듈 로딩 ----------------------------------
import pandas as pd

# 데이터 준비 --------------------------------
list_data = [[1,2,3], [4,5,6], [7,8,9], [10, '11', 12]]

# 데이터 객체 생성 ----------------------------
df = pd.DataFrame(list_data)

# 데이터 객체 정보 출력 ------------------------
print(f"type(df) => {type(df)}\ndata=========\n{df}")

# 데이터 객체 속성 출력 ------------------------
# 객체변수명.속성명     df.XXXX
print(f"df.index => {df.index}")
print(f"df.columns => {df.columns}")
print(f"df.values => \n{df.values}")
print(f"df.shape => \n{df.shape}")
print(f"df.shape => \n{df.dtypes}")

# 데이터 객체 간략 정보 출력 --------------------
df.info()

# 데이터 객체의 인덱스명, 컬럼명 설정 -------------
df.index['ONE', 'TWO', 'THR', 'FOU']
df.columns = ['1ST', '2ND', '3TH']
df.info()