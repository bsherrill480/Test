import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#fgbg = cv2.createBackgroundSubtractorMOG()
ret, prev = cap.read()
ret, curr = cap.read()
prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
curr = cv2.cvtColor(curr, cv2.COLOR_BGR2GRAY)
prevResult = np.zeros(curr.shape, dtype=np.uint8)

def BetterAnd(img1, img2):
    return np.logical_and(img1,img2)*255

while(True):
    ret, next = cap.read()
    next = cv2.cvtColor(next, cv2.COLOR_BGR2GRAY)
    d1 = cv2.absdiff(prev, next)
    d2 = cv2.absdiff(curr, next)
    result = cv2.bitwise_and(d1,d2)
    #Our operations on the frame come here
    # fgmask = fgbg.apply(gray)
    # gray = cv2.subtract(frame,frame1)
    # cv2.line(gray,(0,0),(int(cap.get(3)),int(cap.get(4))),255,5)
    # Display the resulting frame
    ret, result = cv2.threshold(result, 35, 255, cv2.THRESH_BINARY)
    #AND = BetterAnd(result,prevResult).astype(np.uint8)
    cv2.imshow('frame',result)
    prevResult = result
    prev, curr = curr, next
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



