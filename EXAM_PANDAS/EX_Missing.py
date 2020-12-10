# -----------------------------------------------------
# Titanic  Dataset을 활용한 누락 데이터 처리 실습
# -----------------------------------------------------
# 모듈로딩 ---------------------------------------------
import seaborn as sns

#- 써드파티션 Dataset 로딩 ------------------------------
df=sns.load_dataset('titanic')

# (1) 데이터 확인 정보 출력 --------------------------------
df.info()
print(f"df.head() =>\n{df.head()}\n")

# (2) 결측치 체크 ------------------------------------------
print(f"컬럼별 NaN 갯수 =>\n{df.isnull().sum()}\n")

# 결측치 데이터 사전처리 ------------------------------------
# age, deck, embarked, embark-town 4개 컬럼

# age는 age컬럼 평균으로 치환 ------------------------------
mean_age = df['age'].mean(axis=0)             # age 열 평균 계산 (NaN 값 제외)
df['age'].fillna(mean_age, inplace=True)      # age 열 NaN에 평균값 저장

# deck 컴럼은 삭제 ----------------------------------------
df.drop('deck', axis=1, inplace=True)
print(df.head())

# embarked, embark-town 최빈값으로 설정---------------------
#most_embarktown = df['embark_town'].value_counts(dropna=True).idxmax()
most_embarktown = df['embark_town'].value_counts(dropna=True)
print(f"============={type(most_embarktown)} = {most_embarktown}")
most_embark = df['embarked'].value_counts(dropna=True).idxmax()

df['embark_town'].fillna(most_embarktown, inplace=True)
df['embarked'].fillna(most_embark, inplace=True)

print("=========================")
print(df.head())