# 부분추출
# 모듈 로딩 --------------------------------
import cv2
import matplotlib.pyplot as plt

# 데이터 변수 선언 -------------------------------
IMG_NAME = "./image/cat.jpg"
IMG_SAVE = "./image/re_cat.jpg"
DEBUG = True

# (1) 이미지 읽기 --------------------------------
img=cv2.imread(IMG_NAME)
if DEBUG: print('img ={}'.format(img))

# (2) 이미지 잘라내기 -----------------------------
im2=img[150:450, 150:450]

# (3) 잘라낸 이미지 저장 ---------------------------
ret = cv2.imwrite(IMG_SAVE, im2)

if DEBUG: print('ret = {}'.format(ret))
if ret:
    plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    plt.show()
else:
    print('-- SAVE FAIL')