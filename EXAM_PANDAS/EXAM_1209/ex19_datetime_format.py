# 데이터 사전처리 => 시계열 데이터 처리
# -----------------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------------------
import pandas as pd

# 데이터 준비 --------------------------------------------------------------
df = pd.read_csv('../data/stock-data.csv')

# 데이터 사전처리 -----------------------------------------------------------
# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])   #df에 새로운 열로 추가
print(df.head())
print('\n')

# dt 속성을 이용하여 new_Date 열의 년월일 정보를 년, 월, 일로 구분
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())
print('\n')

# Timestamp를 Period로 변환하여 년월일 표기 변경하기
df['Date_ymd'] = df['new_Date'].dt.to_period(freq='D')
print(df.head())
print('\n')

# 원하는 열을 새로운 행 인덱스로 지정
df.set_index('Date_ymd', inplace=True)
print(df.head())


# ========================================================
# # 날짜 인덱스를 이용하여 데이터 선택하기
df_y = df.loc['2018']
print(f"df_y ============>\n{df_y}")

df_ym = df.loc['2018-07']    # loc 인덱서 활용
print(f"df_ym ============>\n{df_ym}")

df_ym_cols = df.loc['2018-07', 'Start':'High']    # 열 범위 슬라이싱
print(f"\ndf_ym_cols ============>\n{df_ym_cols}")

df_ym_cols = df.loc['2018-06', 'Start':'High']    # 열 범위 슬라이싱
print(f"\ndf_ym_cols ============>\n{df_ym_cols}")

df_ymd_range = df['2018-06-25':'2018-06-20']    # 날짜 범위 지정
print(f"\ndf_ymd_range ============>\n{df_ymd_range}")

