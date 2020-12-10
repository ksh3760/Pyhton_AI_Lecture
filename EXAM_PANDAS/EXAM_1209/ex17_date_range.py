# 데이터 사전처리 => 시계열 데이터 처리
# ------------------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------------------
import pandas as pd

# Timestamp의 배열 만들기 - 월 간격, 월의 시작일 기준
ts_ms = pd.date_range( start='2019-01-01',       # 날짜 범위의 시작
                       end=None,                 # 날짜 범위의 끝
                       periods=6,                # 생성할 Timestamp의 개수
                       freq='MS',                # 시간 간격 (MS: 월의 시작일)
                       tz='Asia/Seoul')          # 시간대(timezone)
print(f"ts_ms=>{ts_ms}\n")

# 월 간격, 월의 마지막 날 기준
ts_me = pd.date_range('2019-01-01', periods=6, 
                   freq='M',              # 시간 간격 (M: 월의 마지막 날)
                   tz='Asia/Seoul')       # 시간대(timezone)
print(f"ts_me=>{ts_me}\n")

# 분기(3개월) 간격, 월의 마지막 날 기준
ts_3m = pd.date_range('2019-01-01', periods=6, 
                   freq='3M',             # 시간 간격 (3M: 3개월)
                   tz='Asia/Seoul')       # 시간대(timezone)
print(f"ts_3m=>{ts_3m}\n")
