# -------------------------------------------------------------------------
# 데이터 사전처리 => 범주형 데이터 : 구간 라벨링  ---> One-Hot-Encoding
# ------------------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------------------
import pandas as pd
import numpy as np

# 데이터 준비 --------------------------------------------------------------
# csv ==> DataFrame 형태로 변환
df = pd.read_csv('../data/auto-mpg-02.csv', header=None)

# 데이터 사전처리 (1) ------------------------------------------------------
# (1) 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print('df.columns========>{}\n'.format(df.shape, df.columns))

# (2) horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경

#print('df[horsepower].isnull().sum()========>{}\n'.format( df['horsepower'].isnull().sum()))
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환


# (3) 구간 불할 처리
# (3-1) 3개의 bin으로 나누는 경계 값의 리스트 구하기
print('df[horsepower] ========>\n', df['horsepower'].describe())
bins=[46, 77, 152, 230 ]    # 46~77, 77~152, 152~230

# (3-2) 3개의 bin에 이름 지정
bin_names = [1, 2, 3]

# (3-3) pd.cut 으로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],       # 데이터 배열
                      bins=3,                # 경계 값 리스트
                      labels=bin_names,         # bin 이름
                      include_lowest=True)      # 첫 경계값 포함
print('df[hp_bin] ========>\n',df['hp_bin'])
print('df.columns========>{}\n'.format(df.shape, df.columns))

# (3-4) hp_bin 열의 범주형 데이터를 더미 변수로 변환
horsepower_dummies = pd.get_dummies(df['hp_bin'], prefix='hp')
print('df.columns ========>\n',df.shape, df)
print('horsepower_dummies.head() ========>\n',horsepower_dummies.head())

df2=pd.concat([df, horsepower_dummies], axis=1)
print('NEW df2 1========> {}\n{}\n'.format(df2.shape, df2.columns))
print(df2.head(10))

df2.drop('horsepower', axis=1, inplace=True)
print('NEW df2 2========> {}\n{}\n'.format(df2.shape, df2.columns))
print(df2.head(10))

