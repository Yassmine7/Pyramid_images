import cv2
import numpy as np

img = cv2.imread("pyramides_egypt.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)
    cv2.imshow(str(i), layer)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()