# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2

def empty_func():
    pass

img = np.zeros((512,512,3), np.uint8)
windowName = "Color Pallete"
cv2.namedWindow(windowName)
    
cv2.createTrackbar("B", windowName, 0, 255, empty_func)
cv2.createTrackbar("G", windowName, 0, 255, empty_func)
cv2.createTrackbar("R", windowName, 0, 255, empty_func)
def main():
    while(True):
        cv2.imshow(windowName, img)
        
        if cv2.waitKey(1) == 27:
            break
        
        blue = cv2.getTrackbarPos("B", windowName)
        green = cv2.getTrackbarPos("G", windowName)
        red = cv2.getTrackbarPos("R", windowName)
        img[:] = [blue, green, red]
        
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()