# -------------------------------------------------------
# Series 객체 생성
# 데이터 : 리스트 데이터
# -------------------------------------------------------

# 모듈 로딩 -----------------------------------------------
import pandas as pd

# 데이터 준비 ----------------------------------------------
listdata = ['2020-11-30', 3.14, "Good", 7, True]
listdata1 = [10, 20, 30, 40]

# 객체 만들기 ----------------------------------------------
mySeries = pd.Series(listdata, index=["date", "fvalue", "msg", "dvalue", "bool"])
mySeries1 = pd.Series(listdata1)

# 객체 확인하기 ---------------------------------------------
print(f"type(mySeries) = {type(mySeries)}")
print(f"mySeries data => \n{mySeries}")

print(f"type(mySeries) = {type(mySeries1)}")
print(f"mySeries data => \n{mySeries1}")

# 객체 index, values 속성 확인 -------------------------------
print(f"mySeries.index = {mySeries.index}")
print(f"mySeries.index = {mySeries.values}")

# 객체 속성 변경 ---------------------------------------------
# mySeries1.index = ['greeting1', 'greeting2', 'greeting3']

# 객체 원소(요소) 값 읽기 -------------------------------------
print(f"mySeries[0] = {mySeries[0]}, mySeries1[0] = {mySeries1[0]}")
#print(f"mySeries['date'] = {mySeries['date']}, mySeries1['greeting1'] = {mySeries1['greeting1']}")

# 객체에서 여러개 원소 값 읽기 ----------------------------------
# 리스트 방법 => 연속된 요소가 아닌 경우
print(f"mySeries[[0, 3]] => \n{mySeries[[0, 3]]}")

# 슬라이싱 방법 => 연속된 요소 읽기
print(f"mySeries[1: 4] => \n{mySeries[1: 4]}")
print(f"mySeries['fvalue':'dvalue']=>\n{mySeries['fvalue':'dvalue']}")  # 이름으로 가져오기
