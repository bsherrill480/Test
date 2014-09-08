import numpy as np
import cv2

Ones = np.ones((5,5), dtype=np.uint8)
Zeros = Ones - 1
Twos = Ones + 1
test = Ones
test[0,0] = 2
print np.logical_and(Ones,Ones) * 2
#print test