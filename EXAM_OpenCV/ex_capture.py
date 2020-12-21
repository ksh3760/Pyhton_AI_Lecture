# 패키지 모듈 추가 --------------------------------------------------------------
import cv2
import time

# 데이터변수선언 ------------------------------------------------
HAAR_CASCADE = "haarcascade_frontalface_default.xml"

# 캐스케이드 파일 지정해서 검출기 생성
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + HAAR_CASCADE)

# 카메라 캡쳐하기 ---------------------------------------------------------------
cap = cv2.VideoCapture(0)  # video* 번호  // 괄호내에 영상경로를 넣어서 사용가능  

while (cap.isOpened()):  # 카메라 초기화 및 연결 여부
    ret, img = cap.read()  # 촬영 여부 및 데이터

    if ret:
        # 얼굴 인식하기
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_list = cascade.detectMultiScale(img_gray,
                                             scaleFactor=1.3,
                                             minNeighbors=8)
        # 인식한 부분 표시하기
        for (x, y, w, h) in face_list:
            print("얼굴의 좌표 =", x, y, w, h)
            red = (0, 0, 255)
            cv2.rectangle(img, (x, y), (x + w, y + h), red, thickness=5)

        # 이미지 출력
        cv2.imshow('[ INPUT CAMERA ]', img)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC 키 입력 처리
            cv2.imwrite('./Data/cam/camera.jpg', img)  # 촬영 사진 저장
            break
    else:
        print('no camera~!')
        break

# 카메라 캡쳐 해제 --------------------------------------------------------------
cap.release()
cv2.destroyAllWindows()