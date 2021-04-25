import cv2

# print("opencv-python version = ", cv2.__version__)

# img = cv2.imread('./example/Lenna.png', cv2.IMREAD_COLOR) # Color Image Load
img = cv2.imread('./example/Lenna.png', cv2.IMREAD_GRAYSCALE) # Grayscale Image Load
print(img.shape)
cv2.imshow("Lenna", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('result.png', img)