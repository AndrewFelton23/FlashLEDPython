from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject("/dev/cu.usbmodem1431401")


while True:
    arduino.sendData([1])
    sleep(3)
    arduino.sendData([0])
    sleep(1)
