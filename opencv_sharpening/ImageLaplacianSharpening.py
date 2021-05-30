import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

save_path = './opencv_sharpening/result'

if not os.path.exists(save_path) : os.makedirs(save_path)

image_root_path = 'example/Ch3'
image_path = os.path.join(image_root_path, 'Fig0338(a)(blurry_moon).tif')
print(image_path)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None : 
    print("Image is not loaded.")
    sys.exit(-1)

fig, ax = plt.subplots(1, 3)

ax[0].imshow(image, cmap='gray')
ax[0].axis('off')

laplacian = cv2.Laplacian(image, cv2.CV_8U, ksize=1)
ax[1].imshow(laplacian, cmap='gray')
ax[1].axis('off')

result = image - laplacian
ax[2].imshow(result, cmap='gray')
ax[2].axis('off')

plt.tight_layout()
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
plt.show()