# 모듈로딩 ------------------------------------
import random
import os

# 데이터 변수 선언 -----------------------------
BMI_CSV= '../../DATA/BMI/'

# 데이터 가공 ----------------------------------
def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "normal"
    return "fat"

# 비반도 파일 생성 -------------------------------------
if not os.path.exists(BMI_CSV): os.mkdir(BMI_CSV)

with open(BMI_CSV+'bmi.csv', mode='w',encoding="utf-8") as fp:
    fp.write("height,weight,label\r\n")

    # 무작위로 데이터 생성 ------------------------------------
    cnt = {"thin":0, "normal":0, "fat":0}
    for i in range(20000):
        h = random.randint(120,200)   # 키 범위 지정 랜덤 120 ~ 200 사이 난수 발생
        w = random.randint(35, 80)    # 몸무게 범위 지정 랜덤 35 ~ 80 사이 난수 발생
        label = calc_bmi(h, w)        # 비만도 라벨
        cnt[label] += 1
        fp.write("{0},{1},{2}\r\n".format(h, w, label))
    print("ok,", cnt)