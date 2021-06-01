import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(3)) # 가로 길이 가져오기 
height = int(cap.get(4)) # 세로 길이 가져오기
fps = 30
roi_vector = np.array([[150, 10, 10]])
D0 = 150
while (True) :
    ret, frame = cap.read()
    rgb_mask = np.zeros_like(frame)
    if ret :
        index = np.where(np.sqrt((roi_vector[:, 0] - frame[:, :, 0]) ** 2 + (roi_vector[:, 1] - frame[:, :, 1]) ** 2 + (roi_vector[:, 2] - frame[:, :, 2]) ** 2) <= D0)
        rgb_mask[index[0], index[1]] = 1
        hand_rgb = frame * rgb_mask


        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        s_mask = cv2.inRange(s, 50, 150)
        hand = cv2.bitwise_and(hsv, hsv, mask = s_mask)
        hand = cv2.cvtColor(hand, cv2.COLOR_HSV2BGR)

        cv2.imshow('result', frame)
        cv2.imshow('HSV Color Space', cv2.hconcat([h, s, v]))
        cv2.imshow('Hand Saturation Mask', s_mask)
        cv2.imshow('Hand Segment using HSV Color Space', hand)
        cv2.imshow('Hand RGB Mask', rgb_mask * 255)
        cv2.imshow('Hand Segment using RGB Color Space', hand_rgb)

        if cv2.waitKey(1) & 0xFF == ord('q') : break
    else :
        print("Fail to read frame!")
        break

cap.release()
cv2.destroyAllWindows()