#Based on Zed code - Person Fall detection using raspberry pi camera and opencv lib. Link: https://www.youtube.com/watch?v=eXMYZedp0Uo

import cv2
import time

fitToEllipse = False
cap = cv2.VideoCapture('video-fall-detection/queda.mp4')
time.sleep(2)

fgbg = cv2.createBackgroundSubtractorMOG2()
j = 0

while(1):
    ret, frame = cap.read()

    #Convert each frame to gray scale and subtract the background
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fgmask = fgbg.apply(gray)

        #Find contours
        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:

            # List to hold all areas
            areas = []

            for contour in contours:
                ar = cv2.contourArea(contour)
                areas.append(ar)

            max_area = max(areas, default = 0)

            max_area_index = areas.index(max_area)

            cnt = contours[max_area_index]

            M = cv2.moments(cnt)

            x, y, w, h = cv2.boundingRect(cnt)

            cv2.drawContours(fgmask, [cnt], 0, (255,255,255), 3, maxLevel = 0)

            if h < w:
                j += 1

            if j > 10:
                print("FALL" + str(j))
                cv2.putText(frame, 'Fall Detected', (x-5, y-5), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 3)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

            if h > w:
                j = 0
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


            cv2.imshow('video', frame)

            if cv2.waitKey(33) == 27:
                break
    except Exception as e:
        break
cv2.destroyAllWindows()
