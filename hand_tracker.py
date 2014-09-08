import numpy as np
import cv2
from time import sleep

class BackgroundRemoverThresh:
    def __init__(self, background = None):
        """
        if cap is background, used cv2.VideoCaputure(0) (default cam) to build bg
        returns numpy ndarray, e.g. cv2.VideoCapture object
        """
        if not background:
            self.background = self.build_background()

    def build_background(self, cap = None):
        """builds background from cap, assumes static background in camera feed
           takes 5 seconds to build => no movement for 5 seconds
           if no cap is provided, uses v2.VideoCaputure(0) (default cam)
        """
        capGiven = cap is not None
        if not capGiven:
            cap = cv2.VideoCapture(0)
        #cap.get(4) returns height, cap.get(3) returns width
        #shape is formatted (Height,Width)
        #shape is (H,W,3) where 3 is RGB
        background = np.zeros(shape = (cap.get(4), cap.get(3), 3), dtype=np.float)
        #how to build background can be fine tuned later (or changed to passed params)
        for i in xrange(10):
            ret, frame = cap.read()
            background = background + .1 * frame # builds average
            sleep(.1)
        #docs say to release cap when done
        if not capGiven:
            cap.release()
        return background.astype(dtype=np.uint8)



    def __call__(self, image):
        diff = cv2.absdiff(image, self.background)
        maxRGBDiff = np.maximum(diff[:,:,0],diff[:,:,1],diff[:,:,2])
        thresh1 = cv2.threshold(maxRGBDiff, 40, 255, cv2.THRESH_BINARY)[1]
        #kept for testing
        #thresh2 = cv2.adaptiveThreshold(maxRGBDiff, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        #thresh3 = cv2.adaptiveThreshold(maxRGBDiff, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

        return thresh1

    def max_RGB_difference(self):
        return np.maximum(self.background[:,:,0],self.background[:,:,1],self.background[:,:,2])



def display_image(self, img):
        """for testing purposes"""
        while(True):
            cv2.imshow("frame", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == "__main__":
    background_remover = BackgroundRemoverThresh()
    cap = cv2.VideoCapture(0)

    while(True):
        ret, cur = cap.read()
        img = background_remover(cur)
        kernel = np.ones((3,3),np.uint8)

        cv2.imshow("frame0", cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()