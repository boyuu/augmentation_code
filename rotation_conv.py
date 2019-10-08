import cv2
import numpy as np
import math
import os

def rotation_onepoint(x, y, center_x, center_y, alpha):
    r_x = x-center_x
    r_y = y-center_y
    x2 = r_x*math.cos(alpha*math.pi/180)-r_y*math.sin(alpha*math.pi/180)
    y2 = r_x*math.sin(alpha*math.pi/180)+r_y*math.cos(alpha*math.pi/180)
    r_x = x2 + center_x
    r_y = y2 + center_y
    return (int(r_x),int(r_y))

def rotation_coordinate(x_min, y_min, x_max, y_max, center_x, center_y, angle):
    left_top = rotation_onepoint(x_min, y_min, center_x, center_y, -angle)
    left_bottle = rotation_onepoint(x_min, y_max, center_x, center_y, -angle)
    right_top = rotation_onepoint(x_max, y_min, center_x, center_y, -angle)
    right_bottle = rotation_onepoint(x_max, y_max, center_x, center_y, -angle)

    x_mi = left_top[0]
    x_ma = left_top[0]
    if left_bottle[0] < x_mi:
        x_mi = left_bottle[0]
    if left_bottle[0] > x_ma:
        x_ma = left_bottle[0]
    if right_top[0] < x_mi:
        x_mi = right_top[0]
    if right_top[0] > x_ma:
        x_ma = right_top[0]
    if right_bottle[0] < x_mi:
        x_mi = right_bottle[0]
    if right_bottle[0] > x_ma:
        x_ma = right_bottle[0]
    y_mi = left_top[1]
    y_ma = left_top[1]
    if left_bottle[1] < y_mi:
        y_mi = left_bottle[1]
    if left_bottle[1] > y_ma:
        y_ma = left_bottle[1]
    if right_top[1] < y_mi:
        y_mi = right_top[1]
    if right_top[1] > y_ma:
        y_ma = right_top[1]
    if right_bottle[1] < y_mi:
        y_mi = right_bottle[1]
    if right_bottle[1] > y_ma:
        y_ma = right_bottle[1]

    return x_mi, y_mi, x_ma, y_ma




def process(angle):
    with open('/home/boyu/temperory_result/train.txt') as reader:
        imgsList = reader.readlines()
    for img in imgsList:
        details = img.split()
        img_path = details[0]
        fileName = img_path.split('/')[-1].split('.')[0] + '_{}.jpg'.format(angle)
        buffer = ''
        buffer += '/home/boyu/temperory_rotation/{} '.format(fileName)
        picture = cv2.imread(img_path)
        M = cv2.getRotationMatrix2D((np.shape(picture)[0] / 2, np.shape(picture)[1] / 2), angle, 1.0)
        changed_pic = cv2.warpAffine(picture,M,(np.shape(picture)[0],np.shape(picture)[1]))
        for i in range(len(details)-1):
            bbox = details[i+1].split(',')
            x_min = int(bbox[0])
            y_min = int(bbox[1])
            x_max = int(bbox[2])
            y_max = int(bbox[3])
            rxm, rym, rxma, ryma = rotation_coordinate(x_min,y_min,x_max,y_max,np.shape(picture)[0]/2,np.shape(picture)[1]/2,angle)
            buffer += '{},{},{},{},0 '.format(rxm,rym,rxma,ryma)

            # cv2.rectangle(changed_pic,(rxm,rym),(rxma,ryma),(0,0,255),2)
        cv2.imwrite('/home/boyu/temperory_rotation/{}'.format(fileName),changed_pic)
        buffer += '\n'
        with open('/home/boyu/temperory_rotation/train.txt','a') as writer:
            writer.write(buffer)
        print(buffer)

process(90)
process(180)
process(270)
# for i in range(359):
#     process(i+1)
