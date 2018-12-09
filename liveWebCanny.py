# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:50:45 2018

@author: Anjali
"""

import cv2  
  
#import numpy as np 
  
cap = cv2.VideoCapture(0) 
  
while(1): 
  
    ret, frame = cap.read() 
  
    cv2.imshow('Original',frame) 
  
    edges = cv2.Canny(frame, 100,200) 
  
    cv2.imshow('Edges',edges) 
  
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
cap.release() 
cv2.destroyAllWindows() 