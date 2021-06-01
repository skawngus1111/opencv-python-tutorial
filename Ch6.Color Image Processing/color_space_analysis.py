import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D

img = cv2.imread('./result/screenshot1.png', cv2.COLOR_BGR2RGB) # Grayscale Image Load
# cv2.imshow("Hand", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

r, g, b = cv2.split(img)
print(img.shape)
pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))

fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection='3d')
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()
axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()