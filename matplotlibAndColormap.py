# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:43:33 2018

@author: Anjali
"""
import cv2
import matplotlib.pyplot as plt
def main():
    imgpath = "F:\\opencv\\misc\\4.2.03.tiff"
    img = cv2.imread(imgpath, 1)
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title("BGR")
    plt.show()
    
    plt.imshow(img1)
    plt.title("RGB")
    plt.show()
if __name__ ==  "__main__":
    main()