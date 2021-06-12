import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

save_path = './Ch3.Intensity Transformations and Spatial Filtering/opencv_histogram/result'

if not os.path.exists(save_path) : os.makedirs(save_path)

image = cv2.imread('./example/low_cont.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist(image, [0], None, [256], [0, 256])
histeq_image = cv2.equalizeHist(image)
histeq_image_hist = cv2.calcHist(histeq_image, [0], None, [256], [0, 256])

fig, ax = plt.subplots(2, 2)
ax[0, 0].imshow(image, cmap='gray'); 
ax[0, 0].axis('off')

ax[0, 1].bar(np.arange(hist.shape[0]), np.squeeze(hist))
ax[0, 1].set_yticks([])

ax[1, 0].imshow(histeq_image, cmap='gray'); 
ax[1, 0].axis('off')

ax[1, 1].bar(np.arange(histeq_image_hist.shape[0]), np.squeeze(histeq_image_hist))
ax[1, 1].set_yticks([])

plt.tight_layout()
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
plt.savefig(os.path.join(save_path, 'Image Histogram Equalization.png'), bbox_inches = 'tight', pad_inches = 0)