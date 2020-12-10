# -------------------------------------------------------------------------
# 데이터 사전처리 => 구간분할 : 수치데이터 => 범주형 데이터
# ------------------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------------------
import pandas as pd
import numpy as np


# 데이터 준비 --------------------------------------------------------------
# csv ==> DataFrame 형태로 변환
df = pd.read_csv('../data/auto-mpg-02.csv', header=None)


# 데이터 사전처리 ------------------------------------------------------
# (1) 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# (2) horsepower 열의 누락 데이터('?') 삭제하고 실수형 변환 표준화
df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환
print(df['horsepower'].head(15))


# (3) 구간 불할 처리
# (3-1) 3개의 bin으로 나누는 경계 값의 리스트 구하기
print('df[horsepower] ========>\n', df['horsepower'].describe())

# (3-2) 3개의 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

# (3-3) pd.cut 으로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],       # 데이터 배열
                      bins=3,                   # 경계 값 리스트
                      labels=bin_names,         # bin 이름
                      include_lowest=True)      # 첫 경계값 포함

print('df[hp_bin] ========>\n',df[['hp_bin', 'horsepower']].head(10))
print('df.columns========>{}\n'.format(df.shape, df.columns))
print('df[horsepower] 고유값 ========>\n',df['hp_bin'].value_counts())