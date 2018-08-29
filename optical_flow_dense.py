import cv2 as cv
import numpy as np
cap = cv.VideoCapture("test.mp4")
ret, frame1 = cap.read()
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
while(1):
    ret, frame2 = cap.read()
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    next = cv.normalize(next,  next, 0, 255, cv.NORM_MINMAX)
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    # mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
    hsv = next.copy()
    for row in xrange(0,len(flow),25):
        for col in xrange(0,len(flow[0]),25):
            start = (col,row)
            end = (int(col+flow[row,col,0]),int(row+flow[row,col,1]))
            cv.arrowedLine(hsv,start,end,(255))

    # hsv[...,0] = ang*180/np.pi/2
    # hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    # bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
    cv.imshow('frame2',hsv)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv.imwrite('opticalfb.png',frame2)
        cv.imwrite('opticalhsv.png',bgr)
    prvs = next
cap.release()
cv.destroyAllWindows()