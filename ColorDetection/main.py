import cv2
import numpy as np
from utils import get_limits

yellow = [0, 255, 255]  # yellow in BGR colorspace
lower_limit, upper_limit = get_limits(yellow)

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mask for yellow
    mask = cv2.inRange(hsv_frame, lowerb=lower_limit, upperb=upper_limit)
    
    # Clean the mask using morphological operations
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    #cv2.imshow('mask', mask)
    
    # Find contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # only consider sufficiently large objects
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
