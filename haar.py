import cv2
import time
import numpy as np 

video_src = 'queda.mp4'

cap = cv2.VideoCapture(video_src)
fgbg = cv2.createBackgroundSubtractorMOG2()
#fullbody_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_lowerbody.xml')
#fullbody_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_fullbody.xml')
fullbody_cascade = cv2.CascadeClassifier('cascade.xml')

while True:
    ret, img = cap.read()
	
    fgbg.apply(img)
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    person = fullbody_cascade.detectMultiScale(gray,2,2)

    for(x, y, w, h) in person:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()