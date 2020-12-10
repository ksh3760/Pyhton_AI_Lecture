# -------------------------------------------------------------------------
# 데이터 사전처리 => 범주형 데이터 처리 -> 수치데이터로 변환(On-Hot-Encoding)
# ------------------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------------------
import pandas as pd

# 데이터 준비 --------------------------------------------------------------
df = pd.DataFrame([['green', 'M', 10.1, 'class1'],
                   ['red', 'L', 13.5, 'class2'],
                   ['blue', 'XL', 15.3, 'class1']])

# 데이터 구조 확인
df.columns = ['color', 'size', 'price', 'classlabel']
print('df 데이터 -------------------\n', df)


# 데이터 사전처리 ------------------------------------------------------
# (1) size열의 문자형 데이터 ==> 수치형 값 매칭
#size_mapping = {'XL': 3, 'L': 2, 'M': 1}

#df['size'] = df['size'].map(size_mapping)
print('\n수치형 데이터 -------------------\n', df)

# (2) On-hot-Encoding으로 변환
dumm_size=pd.get_dummies(df['size'], prefix='size')
print('\ndumm_size 데이터 -------------------\n', dumm_size)

# (3) On-hot-Encoding 컬럼 데이터프레임 생성
df2=pd.concat([df, dumm_size], axis=1)
print('NEW df2 데이터 -------------------\n', df2)

df2.drop('size', axis=1, inplace=True)
print('NEW df2 데이터 2 -------------------\n', df2)