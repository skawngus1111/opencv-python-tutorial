import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

save_path = './opencv_smoothing/result'

if not os.path.exists(save_path) : os.makedirs(save_path)

image_root_path = 'example/Ch3'
image_path = os.path.join(image_root_path, 'Fig0333(a)(test_pattern_blurring_orig).tif')
print(image_path)
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None : 
    print("Image is not loaded.")
    sys.exit(-1)

fig, ax = plt.subplots(3, 3, figsize=(6, 6))
ax[0, 0].imshow(image, cmap='gray')
ax[0, 0].axis('off')
i, j = 0, 1
for kernelSize in [3, 5, 7, 9, 11, 13, 15, 17] :
    result = cv2.blur(image, (kernelSize, kernelSize))
    ax[i, j].imshow(result, cmap='gray')
    ax[i, j].axis('off')
    j += 1
    if j == 3 :
        i += 1; j = 0
plt.tight_layout()
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
plt.savefig(os.path.join(save_path, 'blur example.png'))