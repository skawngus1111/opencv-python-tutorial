import cv2
import numpy as np
from skimage.util import random_noise

def add_gaussian_noise(image) :
    row,col,ch= image.shape
    mean = 0
    var = 0.1
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

cap = cv2.VideoCapture(0)

width = int(cap.get(3)) # 가로 길이 가져오기 
height = int(cap.get(4)) # 세로 길이 가져오기
fps = 60
while (True) :
    ret, frame = cap.read()
    if ret :
        noisy = np.array(random_noise(frame, mode='gaussian', clip=True) * 255,dtype=np.uint8)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_noise = cv2.cvtColor(noisy, cv2.COLOR_BGR2HSV)

        h, s, v = cv2.split(hsv)
        h_noise, s_noise, v_noise = cv2.split(hsv_noise)

        cv2.imshow('original', frame)
        cv2.imshow('noise', noisy)
        cv2.imshow('HSV channel', cv2.hconcat([h, s, v]))
        cv2.imshow('Noisy HSV channel', cv2.hconcat([h_noise, s_noise, v_noise]))
        if cv2.waitKey(1) & 0xFF == ord('q') : break
    else :
        print("Fail to read frame!")
        break

cap.release()
cv2.destroyAllWindows()