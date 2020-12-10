# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# 데이터 사전처리 => 범주형 데이터 처리 -> 수치데이터로 변환(On-Hot-Encoding)
# ------------------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------------------
import pandas as pd
import numpy as np

if 1:
    #(1) 데이터 준비
    season = pd.DataFrame({'season':['spring', 'summer', 'fall', 'winter', np.nan]}) #마지막 부분은 결측값 처리 예시를 위한 Nan 값을 생성해준다.
    print('season =>\n', season)
    season.info()

    #(2) On-hot-Encoding으로 변환
    dum1=pd.get_dummies(season['season'])
    print('DUM1 =>\n', dum1)

    dum2=pd.get_dummies(season['season'], dummy_na=True)
    print('DUM2 =>\n', dum2)

if 0:
    fruit = pd.DataFrame({'name':['apple', 'banana', 'cherry', 'durian', np.nan],
                          'color':['red', 'yellow', 'red', 'green', np.nan]})
    #예시 데이터 생성
    print( pd.get_dummies(fruit['name']))
    pd.get_dummies(fruit, columns = ['name'])