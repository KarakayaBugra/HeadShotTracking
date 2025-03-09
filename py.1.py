import cv2
import cvzone
from cvzone.FaceDetectionModule import  FaceDetector


cap=cv2.VideoCapture(0)


det = FaceDetector()

while True:

    _, img = cap.read()
    img,bbox =det.findFaces(img,False)
    if bbox:
        #print(bbox)
        cx, cy=bbox[0]['center']
        print(cx,cy)
        cv2.line(img,(0,cy-80),(640,cy-80),(),6)
        cv2.line(img, (cx,0), (cx, 480), (), 6)
        cv2.circle(img,(cx,cy-80),9,(255,0,0),cv2.FILLED)
        cv2.circle(img,(cx,cy-80),26,(0,0,250),3)
        cvzone.putTextRect(img,f'({cx},{cy-80})',(cx+60,cy-100),1.6,2,colorT=(255,255,255),colorR=(255,0,0),border=3,colorB=())
        cvzone.putTextRect(img,'Target Locked!!',(15,40),1.6,2,colorT=(255,255,255),colorR=(0,255,0),border=3,colorB=())
    cv2.imshow("HeadShot Predictor",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



