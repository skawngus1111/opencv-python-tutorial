import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(3)) # 가로 길이 가져오기 
height = int(cap.get(4)) # 세로 길이 가져오기
fps = 60
while (True) :
    ret, frame = cap.read()
    if ret :
        cv2.imshow('original', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') : break
    else :
        print("Fail to read frame!")
        break

cap.release()
cv2.destroyAllWindows()