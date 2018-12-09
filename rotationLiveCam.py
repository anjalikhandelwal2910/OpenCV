# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:06:12 2018

@author: Anjali
"""

import cv2
import time
def main():
    windowname = "Live camera rotation"
    cv2.namedWindow(windowname)
    
    cap = cv2.VideoCapture(0)
    
    if  cap.isOpened():
        ret, frame = cap.read()
    else:
        ret= False
    
    rows, columns, channels = frame.shape
    
    angle = 0
    scale = 0.1
    
    while True:
        ret, frame = cap.read()
        R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, scale)
        angle = angle + 1
        if scale>=2:
            scale = 0.1
            
        else:
            scale = scale + 0.1
        
        output = cv2.warpAffine(frame, R, (columns, rows))
        
        cv2.imshow(windowname, output)
        time.sleep(0.01)
        if cv2.waitKey(1) ==27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()
    
        
    