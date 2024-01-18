import cv2
import numpy as np

image = cv2.imread('buoy.jpg')
gray_im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_im = cv2.medianBlur(gray_im, 5)

circles = cv2.HoughCircles(blurred_im, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=67, param2=17, minRadius=77, maxRadius=80)

if circles is not None : 
    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        x = int(i[0])
        y = int(i[1])
        r = int(i[2])

        center = (x, y)
        diameter = r * 2

        print(f"center : {center}, diameter : {2 * r}")

        cv2.circle(image, center, r, (0, 255, 0), 3)
        cv2.circle(image, center, 2, (0, 255, 0), 5)

        cv2.imshow('result', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print('Circles did not found')
