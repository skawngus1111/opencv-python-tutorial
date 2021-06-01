import cv2
import numpy as np

cap = cv2.VideoCapture(0)
k1 = np.array([[0.7, 0.7, 0.7]])
k2 = np.array([[1.0, 1.0, 0.7]])

width = int(cap.get(3)) # 가로 길이 가져오기 
height = int(cap.get(4)) # 세로 길이 가져오기
fps = 30

while (True) :
    ret, frame = cap.read()
    if ret :
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        hsv1 = cv2.multiply(hsv, k2)
        hsv2 = cv2.multiply(hsv, k1)
        result1 = cv2.cvtColor(hsv1, cv2.COLOR_HSV2BGR)
        result2 = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)

        cv2.imshow('original', frame)
        cv2.imshow('intensity reduction 1', cv2.multiply(frame, k1))
        cv2.imshow('intensity reduction 2', result1)
        cv2.imshow('wrong result', result2)
        if cv2.waitKey(1) & 0xFF == ord('q') : break
    else :
        print("Fail to read frame!")
        break

cap.release()
cv2.destroyAllWindows()