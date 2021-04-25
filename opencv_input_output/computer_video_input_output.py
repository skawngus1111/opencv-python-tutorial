import cv2

cap = cv2.VideoCapture('./example/sample_video.MOV')

width = int(cap.get(3)) # 가로 길이 가져오기 
height = int(cap.get(4)) # 세로 길이 가져오기
fps = 20

fcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter('output.avi', fcc, fps, (width, height))

while (True) :
    ret, frame = cap.read()
    if ret :
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') : break
    else :
        print("Fail to read frame!")
        break

cap.release()
out.release()
cv2.destroyAllWindows()