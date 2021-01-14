# 모듈로딩 ----------------------------------------------
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

# 데이터 변수 선언 -----------------------------------
data_csv = '../DATA/BMI/bmi.csv'

# (1) 키와 몸무게 데이터 구하기 -----------------------------
bmDf = pd.read_csv(data_csv)

# 칼럼(열)을 자르고 정규화
label = bmDf["label"]
w = bmDf["weight"] / 100        # 최대 100kg라고 가정
h = bmDf["height"] / 200        # 최대 200cm라고 가정
wh = pd.concat([w, h], axis=1)  # 컬럼데이터 생성

# (2) 학습 전용 데이터와 테스트 전용 데이터로 나누기 ------------
data_train, data_test, label_train, label_test = \
    train_test_split(wh, label)

# (3) 데이터 학습하기 --------------------------------------
clf = svm.SVC()
clf.fit(data_train, label_train)

# (4) 데이터 예측하기 ------------------------------------------
predict = clf.predict(data_test)

# (5) 결과 테스트하기 ------------------------------------------
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)

#print("clf.predict([153,46]) =\n", clf.predict([[153,46]]))