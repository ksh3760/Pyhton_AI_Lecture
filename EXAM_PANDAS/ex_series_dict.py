# -------------------------------------------------------
# Series 객체 생성
# 데이터 : 딕셔너리 데이터
# -------------------------------------------------------

# 모듈 로딩 -----------------------------------------------
import pandas as pd

# 데이터 준비 ----------------------------------------------
dictdata = {'a': 90, 'b': 80, 'c': 70, 'd': 60, 'f': 50}

# 객체 만들기 ----------------------------------------------
mySeries = pd.Series(dictdata)

# 객체 확인하기 ---------------------------------------------
print(f"type(mySeries) = {type(mySeries)}")
print(f"mySeries data => \n{mySeries}")

# 객체 속성(attribute) 확인하기 ------------------------------
# index, name, values
index = mySeries.index
name = mySeries.name
values = mySeries.values

print(f"index => {index}")
print(f"name => {name}")
print(f"values => {values}")

# 원소(요소) 데이터 읽기 ---------------------------------------
# 시리즈객체변수명[원소번호] 또는 시리즈객체변수명["원소이름"]
print(f"mySeries['a'] = {mySeries['a']}, mySeries[0] = {mySeries[0]}")

# 여러개 원소(요소) 데이터 읽기 ----------------------------------
# (1) 3번인덱스부터 끝까지 데이터 읽기
print(f"mySeries[3:] => \n{mySeries[3:]}")
print(f"mySeries['d':] => \n{mySeries['d':]}")

# (2) 홀수번째 인덱스 데이터 읽기
print(f"mySeries[[1, 3]] => \n{mySeries[list(range(1,5,2))]}")
print(f"mySeries[['b', 'd']] => \n{mySeries[['b', 'd']]}")
