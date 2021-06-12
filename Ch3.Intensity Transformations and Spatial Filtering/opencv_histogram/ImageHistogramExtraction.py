
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

save_path = './Ch3.Intensity Transformations and Spatial Filtering/opencv_histogram/result'

if not os.path.exists(save_path) : os.makedirs(save_path)

light_image = cv2.imread('./example/Ch3/Fig0320(1)(top_left).tif')
gray_image = cv2.imread('./example/Ch3/Fig0320(2)(2nd_from_top).tif')
high_cont_image = cv2.imread('./example/Ch3/Fig0320(3)(third_from_top).tif')
dark_image = cv2.imread('./example/Ch3/Fig0320(4)(bottom_left).tif')

light_hist = cv2.calcHist(light_image, [0], None, [256], [0, 256])
gray_hist = cv2.calcHist(gray_image, [0], None, [256], [0, 256])
high_cont_hist = cv2.calcHist(high_cont_image, [0], None, [256], [0, 256])
dark_hist = cv2.calcHist(dark_image, [0], None, [256], [0, 256])

fig, ax = plt.subplots(2, 4)
ax[0, 0].imshow(light_image, cmap='gray'); 
ax[0, 0].axis('off')

ax[0, 1].imshow(gray_image, cmap='gray'); 
ax[0, 1].axis('off')

ax[0, 2].imshow(high_cont_image, cmap='gray'); 
ax[0, 2].axis('off')

ax[0, 3].imshow(dark_image, cmap='gray'); 
ax[0, 3].axis('off')

ax[1, 0].bar(np.arange(light_hist.shape[0]), np.squeeze(light_hist))
ax[1, 0].set_yticks([])

ax[1, 1].bar(np.arange(gray_hist.shape[0]), np.squeeze(gray_hist))
ax[1, 1].set_yticks([])

ax[1, 2].bar(np.arange(high_cont_hist.shape[0]), np.squeeze(high_cont_hist))
ax[1, 2].set_yticks([])

ax[1, 3].bar(np.arange(dark_hist.shape[0]), np.squeeze(dark_hist))
ax[1, 3].set_yticks([])

plt.tight_layout()
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
plt.savefig(os.path.join(save_path, 'Image Histogram example.png'), bbox_inches = 'tight', pad_inches = 0)