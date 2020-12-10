# --------------------------------------------------------------------
# 데이터 사전처리 => 누락값(Missing Value) 확인
# --------------------------------------------------------------------
# 모듈 로딩 -----------------------------------------------------------
import pandas as pd
import numpy as np                # NaN 표기 사용하기 위해 추가
from   EXAM_PANDAS.util import *

if 1:
    # 데이터 준비  --------------------------------------------------
    data=[ [1.4, np.nan ],
           [7.1, -4.5],
           [np.nan, np.nan],
           [2.9, 1.6],
           [0.4, -3.1]]

    # 데이터 객체 생성 -----------------------------------------------
    df=pd.DataFrame(data,
                    columns=['One', 'Two'],
                    index=['a','b','c', 'd', 'e'])
    displayData("df", df)

    # 데이터 확인 ----------------------------------------------------
    # (1) 데이터 앞 & 뒤 데이터만 출력
    print(f"\ndf.head(3) =>\n {df.head(3)}")
    print(f"\ndf.tail(3) =>\n {df.tail(3)}")

    # (2) 데이터 컬럼별 &행별 데이터 개수 출력
    print(f"\n컬럼별 df.count() =>\n {df.count()}")
    print(f"\n행 별 df.count(axis=1) =>\n {df.count(axis=1)}")

    # (3) 데이터 컬럼별 &행별 데이터 합계, 최소값, 최대값 출력
    print(f"\n컬럼별 df.sum() =>\n {df.sum()}")
    print(f"\n행 별  df.sum(axis=1) =>\n {df.sum(axis=1)}")
    print(f"\n컬럼별 df.min() =>\n {df.min()}")
    print(f"\n행 별  df.min(axis=1) =>\n {df.min(axis=1)}")

    print(f"\n컬럼별 df.max() =>\n {df.max()}")
    print(f"\n행 별  df.max(axis=1) =>\n {df.max(axis=1)}")

    # (4) 컬럼별 NaN데이터 갯수 확인
    print(f"\n컬럼별 df.isnull() =>\n {df.isnull()}")
    print(f"\n컬럼별 df.notnull() =>\n {df.notnull()}")

    # (5)데이터 컬럼별 &행별  NaN 갯수
    print(f"\n컬럼별 df.isnull() =>\n {df.isnull().sum()}")
    print(f"\n컬럼별 df.notnull() =>\n {df.notnull().sum()}")

    print(f"\n행 별 df.isnull() =>\n {df.isnull().sum(axis=1)}")
    print(f"\n행 별 df.notnull() =>\n {df.notnull().sum(axis=1)}")

    # DataFrame 정보 출력
    df.info()

# 데이터 준비 02) ---------------------------------------------------------
if 0:
    # csv => DataFrame 형태
    df = pd.read_csv("../data/auto-mpg-02.csv", header=None)

    # 데이터 사전처리 ------------------------------------------------------
    # 열 이름을 지정
    df.columns = ['mpg','cylinders','displacement',
                  'horsepower','weight','acceleration',
                  'model year','origin','name']

    displayData("df", df)

    # 데이터 구조 확인 ------------------------------------------------------
    # (1) mpg열의 고유값 종류 및 개수 확인
    nan_mpg = df['mpg'].value_counts(dropna=False)
    print('nan_mpg----------\n',nan_mpg)

    # (2) isnull() 메서드로 누락 데이터 찾기
    print('\nisnull() 누락 데이터 찾기 =>\n', df.head().isnull())

    # (3) notnull() 메서드로 누락 아닌 데이터 찾기
    print('\nnotnull() 누락 데이터 찾기 =>\n', df.head().notnull())

    # (4) isnull() 메서드로 누락 데이터 개수 구하기
    print('\n열별 NA인 행들 합 df.isnull().sum(axis=0) =>\n',df.head().isnull().sum())
    print('\n행별 NA인 열들 합 df.isnull().sum(axis=1) =>\n',df.head().isnull().sum(axis=1))