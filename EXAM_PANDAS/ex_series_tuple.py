# -------------------------------------------------------
# Series 객체 생성
# 데이터 : 튜플 데이터
# -------------------------------------------------------

# 모듈 로딩 -----------------------------------------------
import pandas as pd

# 데이터 준비 ----------------------------------------------
listdata = ('2020-11-30', 3.14, "Good", 7, True)
listdata1 = (10, 20, 30, 40)

# 객체 만들기 ----------------------------------------------
mySeries = pd.Series(listdata)
mySeries1 = pd.Series(listdata1)

# 객체 확인하기 ---------------------------------------------
print(f"type(mySeries) = {type(mySeries)}")
print(f"mySeries data => \n{mySeries}")

print(f"type(mySeries) = {type(mySeries1)}")
print(f"mySeries data => \n{mySeries1}")


# 객체 index, values 속성 확인 -------------------------------
print(f"mySeries.index = {mySeries.index}")
print(f"mySeries.index = {mySeries.values}")
