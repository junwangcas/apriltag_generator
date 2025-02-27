#!/usr/bin/env python
# coding: UTF-8
import apriltag
#import pupil_apriltags as apriltag     # for windows
import cv2
import numpy as np
import sys

img =cv2.imread("data/20230427131849.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 创建一个apriltag检测器
#at_detector = apriltag.Detector(apriltag.DetectorOptions(families='tag36h11 tag25h9') )
at_detector = apriltag.Detector()
# at_detector = apriltag.Detector(families='tag36h11 tag25h9')  #for windows
# 进行apriltag检测，得到检测到的apriltag的列表
tags = at_detector.detect(gray)
print("%d apriltags have been detected."%len(tags))
for tag in tags:
    cv2.circle(img, tuple(tag.corners[0].astype(int)), 4,(255,0,0), 2) # left-top
    cv2.circle(img, tuple(tag.corners[1].astype(int)), 4,(255,0,0), 2) # right-top
    cv2.circle(img, tuple(tag.corners[2].astype(int)), 4,(255,0,0), 2) # right-bottom
    cv2.circle(img, tuple(tag.corners[3].astype(int)), 4,(255,0,0), 2) # left-bottom

cv2.imshow("apriltag_test",img)
cv2.waitKey()
