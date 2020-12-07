import cv2
import numpy as np
def nothing(x):
    pass

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H","Trackbars",0,179,nothing)
cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
cv2.createTrackbar("L-V","Trackbars",0,255,nothing)
cv2.createTrackbar("U-H","Trackbars",179,179,nothing)
cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
cv2.createTrackbar("U-V","Trackbars",255,255,nothing)



while True:
    _,frame=cap.read()
    
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    l_h=cv2.getTrackbarPos("L-H","Trackbars")
    l_s=cv2.getTrackbarPos("L-S","Trackbars")
    l_v=cv2.getTrackbarPos("L-V","Trackbars")
    u_h=cv2.getTrackbarPos("U-H","Trackbars")
    u_s=cv2.getTrackbarPos("U-S","Trackbars")
    u_v=cv2.getTrackbarPos("U-V","Trackbars")

    #red
    low=np.array([l_h,l_s,l_v])
    higth=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hsv_frame,low,higth)
    color=cv2.bitwise_and(frame,frame,mask=mask)


    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area=cv2.contourArea(contour)
        if area<1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(color,(x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow("frame",frame)
    cv2.imshow("color",color)

    key=cv2.waitKey(1)
    if key==27:
        break 




