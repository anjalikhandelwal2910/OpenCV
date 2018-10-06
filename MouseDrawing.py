# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 05:54:16 2018

@author: Anjali
"""

import numpy as np
import cv2

img = np.zeros((512, 512,3), np.uint8)    
windowName = "Drawing"
cv2.namedWindow(windowName)

def draw_circle(event, x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 40, (0, 255, 0), -1)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 20, (0, 0, 255), -1)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 20, (98, 213, 173), -1)    
#    events = [i for i in dir(cv2) if "EVENT" in i]
#    print(events)
cv2.setMouseCallback(windowName, draw_circle)
def main():        
    while(True):
        cv2.imshow(windowName, img)
            
        if cv2.waitKey(20) == 27:
            break
        
    cv2.destroyAllWindows()


        
if __name__ == "__main__":
    main()