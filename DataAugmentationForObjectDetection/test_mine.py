from data_aug.data_aug import *
from data_aug.bbox_util import *
import cv2
import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
import random
import os
from tqdm import tqdm

def horizontal_flip(img, bboxes):
    return RandomHorizontalFlip(1)(img.copy(), bboxes.copy())


def scaling(img, bboxes):
    return RandomScale(0.3, diff = True)(img.copy(), bboxes.copy())


def tanslation(img, bboxes):
    return RandomTranslate(0.3, diff = True)(img.copy(), bboxes.copy())


def rotation(angle, img, bboxes):
    return RandomRotate(angle)(img.copy(), bboxes.copy())


def shear(img, bboxes):
    return RandomShear(0.2)(img.copy(), bboxes.copy())


def HSV_tranns(img, bboxes):
    return RandomHSV(100, 100, 100)(img.copy(), bboxes.copy())

# root_dir = '/home/raja/DATA/people_detection/clubbed_data/new_database/label_files'
#
# txt_files = [root_dir + '/train_redo.txt',
#              root_dir + '/val_redo.txt']
#
#
# with open(root_dir + 'train_andVal.txt', 'w') as outfile:
#     for fname in txt_files:
#         with open(fname) as infile:
#             for line in infile:
#                 outfile.write(line)
# outfile.close()
#
# with open(root_dir + 'train_and'
#                      'Val.txt') as reader:
#     imgsList = reader.readlines()
#
# txt_new = root_dir + '/all_withAug.txt'
#
# with open(txt_new, 'w') as writer:
#     for _i, img_name in tqdm(enumerate(imgsList)):
#         writer.write(img_name)
#
#         details = img_name.split()
#         img_path = details[0]
#         dir_path  = os.path.dirname(img_path)
#         single_img_name = os.path.basename(img_path)
#
#         picture = cv2.imread(img_path)
#         all_bbox = []
#         for i in range(len(details)-1):
#             bbox = details[i+1].split(',')
#             x_min = int(bbox[0])
#             y_min = int(bbox[1])
#             x_max = int(bbox[2])
#             y_max = int(bbox[3])
#
#             bboxes_fix = np.hstack((x_min, y_min, x_max, y_max))
#             all_bbox.append(bboxes_fix)
#
#         img = picture
#         raw_boxes = np.array(all_bbox, dtype=float)
#         aug_img, aug_box = random.choice([horizontal_flip(img, raw_boxes),
#                                           scaling(img, raw_boxes),
#                                           tanslation(img, raw_boxes),
#                                           shear(img, raw_boxes),
#                                           HSV_tranns(img, raw_boxes)])
#
#         aug_img_name = single_img_name.split('.jpg')[0] + '_AguOther.jpg'
#         aug_img_path = dir_path + '/' + aug_img_name
#         cv2.imwrite(aug_img_path, aug_img)
#
#         writer.write(aug_img_path + ' ')
#         for one_box in aug_box:
#             for __i, one_point in enumerate(one_box):
#                 writer.write(str(int(one_point)) + ',')
#             writer.write(str(0) + ' ')
#         writer.write('\n')
#
#         angle1 = np.random.randint(-50, -10)
#         angle2 = np.random.randint(10, 20)
#         angle = random.choice([angle1, angle2])
#
#         rot_img, rot_box = rotation(angle, img, raw_boxes)
#         rot_img_name = single_img_name.split('.jpg')[0] + '_AguRot.jpg'
#         rot_img_path = dir_path + '/' + rot_img_name
#         cv2.imwrite(rot_img_path, rot_img)
#         writer.write(rot_img_path + ' ')
#         for one_box in rot_box:
#             for __i, one_point in enumerate(one_box):
#                 writer.write(str(int(one_point)) + ',')
#             writer.write(str(0) + ' ')
#         writer.write('\n')
#
# writer.close()
#
#
# file = open(txt_new, 'r').readlines()
# random.shuffle(file)
# with open(root_dir + '/trainWithAug_redo.txt', 'w') as train_writer:
#     with open(root_dir + '/valWithAug_redo.txt', 'w') as val_wrtier:
#         for i, line in enumerate(file):
#             # dirname = os.path.dirname(line)
#             # imgname = os.path.basename(line)
#
#             if i >= int(0.2 * len(file)):
#                 train_writer.write(line)
#             else:
#                 val_wrtier.write(line)
#     val_wrtier.close()
# train_writer.close()