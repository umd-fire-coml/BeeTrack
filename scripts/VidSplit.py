# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:18:37 2018

@author: Huu (Found on StockOverflow)
"""

import cv2
vidcap = cv2.VideoCapture('RawVid1.mkv') #Change name to fit the video file
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read() # "increments" to next frame
  print('Read a new frame: ', success) #Debugging, shows that there's a next frame
  count += 1#increments to have unique frame name
