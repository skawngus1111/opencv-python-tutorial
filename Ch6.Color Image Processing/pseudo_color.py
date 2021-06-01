import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(3)) # 가로 길이 가져오기 
height = int(cap.get(4)) # 세로 길이 가져오기
fps = 30

while (True) :
    ret, frame = cap.read()
    if ret :
        autumn_color = cv2.applyColorMap(frame, cv2.COLORMAP_AUTUMN)
        jet_color = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
        inferno_color = cv2.applyColorMap(frame, cv2.COLORMAP_INFERNO)

        cv2.imshow('result', frame)
        cv2.imshow('COLORMAP_AUTUMN', autumn_color)
        cv2.imshow('COLORMAP_JET', jet_color)
        cv2.imshow('COLORMAP_INFERNO', inferno_color)

        if cv2.waitKey(1) & 0xFF == ord('q') : break
    else :
        print("Fail to read frame!")
        break

cap.release()
cv2.destroyAllWindows()