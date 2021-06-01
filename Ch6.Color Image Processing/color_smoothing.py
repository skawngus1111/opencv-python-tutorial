import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(3)) # 가로 길이 가져오기 
height = int(cap.get(4)) # 세로 길이 가져오기
fps = 60
kernel_size = 51
while (True) :
    ret, frame = cap.read()
    if ret :
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        v_smoothing = cv2.blur(v, ksize=(kernel_size, kernel_size))
        hsv_smoothing = cv2.merge([h, s, v_smoothing])
        hsv_smoothing = cv2.cvtColor(hsv_smoothing, cv2.COLOR_HSV2BGR)
        rgb_smoothing = cv2.blur(frame, ksize=(kernel_size, kernel_size))

        difference = cv2.cvtColor(cv2.absdiff(rgb_smoothing, hsv_smoothing), cv2.COLOR_BGR2RGB)
        print(difference)

        cv2.imshow('original', frame)
        cv2.imshow('51x51 box smoothing(RGB)', rgb_smoothing)
        cv2.imshow('51x51 box smoothing(Only I)', hsv_smoothing)
        cv2.imshow('difference image', difference)

        if cv2.waitKey(1) & 0xFF == ord('q') : break
    else :
        print("Fail to read frame!")
        break

cap.release()
cv2.destroyAllWindows()