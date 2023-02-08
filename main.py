import cv2
from cvzone.HandTrackingModule import HandDetector

video=cv2.VideoCapture(0)
video.set(3,1080)
video.set(4,720)

detector=HandDetector(detectionCon=0.8)

while True:
    _,frame=video.read()
    lmlist,_=detector.findHands(frame)
    cv2.imshow("video",frame)
    k=cv2.waitKey(1)
    if k == ord("q"):
        break