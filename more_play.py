import numpy as np
import cv2
cap = cv2.VideoCapture(0)
fgbg = cv2.BackgroundSubtractorMOG()
while(1):
    ret, frame = cap.read()
    frame = fgbg.apply(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()