from cv2 import cv2

cam  = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame = cam.read()
    cv2.imshow('Secret Cam', frame)

    cv2. 