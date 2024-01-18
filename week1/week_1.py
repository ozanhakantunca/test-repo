import cv2
import numpy as np

image = cv2.imread('buoy.jpg')
if image is None:
    print('image is not valid')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

upper_yellow = np.array([50, 255, 255])
lower_yellow = np.array([17, 73, 60])

masked_im = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

contours, hierarchy = cv2.findContours(masked_im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

maxArea = 0
MaxBBox = None

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = w * h
    if area > maxArea:
        maxArea = area
        MaxBBox = (x, y, w, h)

if MaxBBox is not None:
    x, y, w, h = MaxBBox
    cv2.rectangle(masked_im, (x , y), (x +w, y+h), (255, 255, 255), 2)

print(f"max area: {maxArea}" )

cv2.imshow('test', masked_im)
cv2.waitKey(0)
cv2.destroyAllWindows()


