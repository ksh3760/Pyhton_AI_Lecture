# 패키지 모듈 추가 --------------------------------------------------------------
import numpy as np
import cv2

# 블랙 배경 이미지 생성 ---------------------------------------------------------
img = np.zeros((512,512,3), np.uint8)

# 5px의 도형 그리기 ------------------------------------------------------------
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,0),-1)

# 다각형 그리기 -----------------------------------------------------------------
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# 텍스트 출력하기 ---------------------------------------------------------------
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hello OpenCV!!!',
            (10,500), font, 2, (255,255,255), 2, cv2.LINE_AA)

# 이미지 출력 및 20초 후 종료--------------------------------------------------
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()