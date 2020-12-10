# ---------------------------------------------------
# HTML >> DataFrame 객체로 변환
# HTML 파일 안에 <table>태그만 DataFrame 담아서 오기
# ---------------------------------------------------
# 라이브러리 로딩 --------------------------------------
import pandas as pd
from EXAM_PANDAS.util import  displayData, displayInfo

# 전역변수 --------------------------------------------
html_path ='../data/sample.html'

# html ==> DataFrame 객체 ---------------------------
tables = pd.read_html(html_path)

# 데이터 확인 ----------------------------------------
displayData("tables",tables)
print(f"type(tables) => {type(tables)}, len(tables) => {len(tables)}")

# 리스트 안에 요소 모두 확인
for table in tables:
    print(f"type(table) => {type(table)}\n{table}")

# 2번째 테이블에 저장된 데이터 가져와서 출력 --------------
displayData("tables[1]", tables[1])

# name 컬럼을 행인덱스로 설정 --------------------------
tables[1].set_index('name', inplace=True)
displayData("\ntables[1] - set_index('name')", tables[1])

# 정렬하기--------------------------------------------
# 행인덱스 기준 내림차순 정렬
ndf=tables[1].sort_index(ascending=False)
displayData("\nndf - sort_index(ascending=False)", ndf)

# year로 오름차순 정렬
ndf2=tables[1].sort_values(by='year')
displayData("\nndf2 - sort_values(by='year')", ndf2)








if 0:
    # tables 리스트의 원소를 iteration 각각 화면 출력
    for i in range(len(tables)):
        print("tables[%s]" % i)
        print(tables[i])
        print('\n')

    # 파이썬 패키지 정보가 들어 있는 두 번째 데이터프레임을 선택하여 df 변수에 저장
    df = tables[1]

    # 'name' 열을 인덱스로 지정
    df.set_index(['name'], inplace=True)
    print(df)