# coding=utf-8

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../gludoc_ios/assets/images/148_2.png',cv2.IMREAD_COLOR)

b, g, r = cv2.split(img)
img2 = cv2.merge([r , g, b])

plt.imshow(img2)
plt.xticks([])
plt.yticks([])
plt.show()

# cv2.imshow("title", gray)
# cv2.waitKey(0)
# cv2.destroyWindow()

