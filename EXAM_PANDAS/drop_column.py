# ==========================================================
# 열(column) 삭제
# df객체변수명.drop(열이름, axis=1, inplace=False)
# ==========================================================
import pandas as pd

# 전역변수 ---------------------------------------------------
DEBUG = True  # 개발 중에만 사용

# 데이터 준비 ------------------------------------------------
exam_data = {'수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

# 데이터 객체 생성 --------------------------------------------
df = pd.DataFrame(exam_data);

# 인덱스 설정 ------------------------------------------------
df.index = ['학생1', '학생2', '학생3']

if DEBUG:
    # 데이터 객체 정보 출력 - 인덱스, 컬럼, 형태, 데이터
    print(f"df.index => {df.index}")
    print(f"df.columns => {df.columns} ")
    print(f"d => {df.shape}")
    print(f"df => {df}")

# 컬럼 삭제하기 -------------------------------------------------
# 1개 컬럼 삭제
ndf1 = df.drop('음악', axis=1)
print(f"d => {ndf1.shape}")
print(f"df => {ndf1}")

# 2개 컬럼 삭제
ndf2 = df.drop(['영어', '체육'], axis=1)
print(f"ndf2.shape => {ndf2.shape}")
print(f"ndf2 => {ndf2}")

# 행 삭제하기 ----------------------------------------------------
# 1개 행(row) 삭제
ndf3 = df.drop('학생1')
print(f"ndf3.shape => {ndf3.shape}")
print(f"ndf3 => {ndf3}\n")

# 2개 행(row) 삭제
ndf4 = df.drop(['학생1', '학생3'])
print(f"ndf4.shape => {ndf4.shape}")
print(f"ndf4 => {ndf4}\n")

ndf5 = df.drop(['학생1', '학생3'], inplace=True)
print(f"ndf5.shape => {ndf5}")
print(f"df => {df}\n")
