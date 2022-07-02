import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("cat3.jpg")
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.axis('off')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
k = np.ones((5, 5), dtype=np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, k, iterations=2)
distTransform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, fore = cv2.threshold(distTransform, 0.2 * distTransform.max(), 255, 0)
bg = cv2.dilate(opening, k, iterations=20)
fore = np.uint8(fore)
ret, markets = cv2.connectedComponents(fore)
unknown = cv2.subtract(bg, fore)
markets = markets + 1
markets[unknown == 255] = 0
markets = cv2.watershed(img, markets)
img[markets == -1] = [255, 0, 0]

plt.subplot(122)
plt.imshow(img, cmap="gray")
plt.axis('off')
plt.show()