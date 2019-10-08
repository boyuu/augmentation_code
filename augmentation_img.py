import cv2
import numpy as np
import os
from DataAugmentationForObjectDetection.test_mine import *

save_path = '/home/boyu/temperory_aug/'
with open('/home/boyu/temperory_rotation/train.txt') as reader:
    imgsList = reader.readlines()
with open(save_path + 'train.txt', 'a') as writer:
    for img in imgsList:
        details = img.split()
        img_path = details[0].strip()
        picture = cv2.imread(img_path)
        all_bbox = []
        len_signal = 0
        for i in range(len(details) - 1):
            bbox = details[i + 1].split(',')
            x_min = int(bbox[0])
            y_min = int(bbox[1])
            x_max = int(bbox[2])
            y_max = int(bbox[3])
            tp = int(bbox[4])
            if tp == 0:
                bboxes_fix = np.hstack((x_min, y_min, x_max, y_max))
                all_bbox.append([x_min, y_min, x_max, y_max])
                # cv2.rectangle(picture,(x_min,y_min),(x_max,y_max),(255,0,0),2)
            elif tp == 1:
                cv2.rectangle(picture,(x_min,y_min),(x_max,y_max),(0,0,255),2)
        if len(all_bbox) == 0:
            len_signal = 1
            all_bbox.append([1,1,2,2])
        raw_boxes = np.array(all_bbox, dtype=float)
        # aug_img, aug_box = random.choice([horizontal_flip(picture, raw_boxes),
        #                                 scaling(picture, raw_boxes),
        #                                 tanslation(picture, raw_boxes),
        #                                 shear(picture, raw_boxes),
        #                                 HSV_tranns(picture, raw_boxes)])
        aug_img, aug_box = random.choice([HSV_tranns(picture, raw_boxes)
                                        ])

        buffer = save_path+'HSV_'+img_path.split('/')[-1]+' '
        if len_signal == 0:
            for box in aug_box:
                buffer += str(int(box[0])) + ',' + str(int(box[1])) + ',' + str(int(box[2])) + ',' + str(int(box[3])) + ',' + '0 '
        buffer += '\n'
        cv2.imwrite(save_path+'HSV_'+img_path.split('/')[-1],aug_img)
        # cv2.imshow('img', aug_img)
        # cv2.waitKey(0)
        print(buffer)
        writer.writelines(buffer)