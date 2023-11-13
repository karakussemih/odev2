#Semih Karakuş
#02195076064



import cv2
import numpy as np


kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()

    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

    lower1 = np.array([0, 100, 100])
    upper1 = np.array([10, 255, 255])

    lower2 = np.array([160, 100, 100])
    upper2 = np.array([179, 255, 255])

    lower_mask = cv2.inRange(hsv, lower1, upper1)
    upper_mask = cv2.inRange(hsv, lower2, upper2)

    mask = lower_mask+upper_mask

    maskelenmisGoruntu = cv2.bitwise_and(goruntu, goruntu, mask=mask)
    #maskelenmisGoruntu[np.where((maskelenmisGoruntu > [0, 0, 0]).all(axis=2))] = [255, 255, 255]

    cv2.imshow("Kamera", maskelenmisGoruntu)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()