import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(3)) # 가로 길이 가져오기 
height = int(cap.get(4)) # 세로 길이 가져오기
fps = 30

while (True) :
    ret, frame = cap.read()
    if ret :
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        ycbcr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

        B_channel = frame[:, :, 0]
        G_channel = frame[:, :, 1]
        R_channel = frame[:, :, 2]
        
        H_channel = hsv[:, :, 0]
        S_channel = hsv[:, :, 1]
        V_channel = hsv[:, :, 2]

        Y_channel = ycbcr[:, :, 0]
        Cr_channel = ycbcr[:, :, 1]
        Cb_channel = ycbcr[:, :, 2]

        cv2.imshow('result', frame)
        cv2.imshow('BGR channel', cv2.hconcat([B_channel, G_channel, R_channel]))
        cv2.imshow('HSV channel', cv2.hconcat([H_channel, S_channel, V_channel]))
        cv2.imshow('YCrCb channel', cv2.hconcat([Y_channel, Cr_channel, Cb_channel]))

        if cv2.waitKey(1) & 0xFF == ord('q') : break
    else :
        print("Fail to read frame!")
        break

cap.release()
cv2.destroyAllWindows()