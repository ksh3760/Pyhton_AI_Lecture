"""
    DataFrame 데이터 정보, 데이터 출력 기능 함수
"""

def displayInfo(dfname, df):
    #객체 속성 정보 출력 --------------------------------------
    print(f'---------------{dfname}---------------')
    print(f'df.index = {df.index}')
    print(f'df.columns = {df.columns}')
    print(f'df.shape = {df.shape}')
    print(f'df.dtypes = {df.dtypes}\n')

    # 데이터 객체 정보 출력 ------------------------------------
    df.info()

def displayData(dfname, df):
    # 객체 속성 정보 출력 --------------------------------------
    print(f'id : {id(df)}')
    print(f'{dfname} DATA ===========================\n{df}')
