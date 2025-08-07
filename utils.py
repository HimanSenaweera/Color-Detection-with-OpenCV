import numpy as np
import cv2

def get_limits(color):
    #Converts the input color into a 1×1×3 image required because cv2.cvtColor() needs an image-like array.
    c = np.uint8([[color]])  
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    #hsvC[0][0][0] gives the Hue value.We create a range of ±10 around that Hue value.
    lowerLimit = hsvC[0][0][0] - 10, 100, 100 
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
