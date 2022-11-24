from cvzone.SerialModule import SerialObject
from time import sleep
import cv2

arduino = SerialObject("/dev/cu.usbmodem1431401")

# imgLEDOn = cv2.imread("../Resources/LedOn.jpg")
# imgLEDOff = cv2.imread("../Resources/LedOff.jpg")
imgLEDOn = cv2.imread("../Resources/Pin13On.jpg")
imgLEDOff = cv2.imread("../Resources/Pin13Off.jpg")

while True:
    arduino.sendData([1])
    cv2.imshow("../Image",imgLEDOn)
    cv2.waitKey(3000)
    sleep(3)
    arduino.sendData([0])
    cv2.imshow("../Image",imgLEDOff)
    cv2.waitKey(1000)
    sleep(1)