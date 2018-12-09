# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:45:44 2018

@author: Anjali
"""

import cv2
def main():
    windowName = "opencv Video Player"
    cv2.namedWindow(windowName)
    filename = "F:\OpenCVProjects/Webcamrecord.avi"
    
    cap = cv2.VideoCapture(filename)
    count = 0
    
    def onchange():
        pass
    
    cv2.createTrackbar("speed", windowName, 17, 66, onchange)
    while (cap.isOpened()):
        ret, frame = cap.read()
        #print(ret)
        #count = count+1
        if ret:
            cv2.imshow(windowName, frame)
            s = cv2.getTrackbarPos('speed', windowName)
            if cv2.waitKey(s) == 27:
                break
        else:
            break        
    cv2.destroyAllWindows()
    cap.release()
    print(count)
if __name__ == "__main__":
    main()