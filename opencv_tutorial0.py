import cv2

# print("opencv-python version = ", cv2.__version__)

img = cv2.imread('./example/Einstein.jpg')
print(img.shape)
cv2.imshow("Example Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()