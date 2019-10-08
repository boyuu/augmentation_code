import cv2
import os
import numpy as np
import json
import xml.etree.ElementTree as ET
fileList_reader = os.popen('cd /home/boyu/temperory_result; ls')
fileList = fileList_reader.read().split()
with open('/home/boyu/temperory_result/train.txt','w') as writer:
    for file in fileList:
        if not file.endswith('.xml'):
            continue
        # if not ((int(file.split('.')[0].strip()) >= 411 and int(file.split('.')[0].strip()) <= 419) or (int(file.split('.')[0].strip()) >= 641 and int(file.split('.')[0].strip()) <= 751) or (int(file.split('.')[0].strip()) >= 787 and int(file.split('.')[0].strip()) <= 807) or (int(file.split('.')[0].strip()) >= 813 and int(file.split('.')[0].strip()) <= 857)):
        #     print('########################################################')
        #     continue
        file_path = '/home/boyu/temperory_result/{}'.format(file)
        buffer = ''
        if file.endswith('.json'):
            buffer += '/home/boyu/temperory_annotation/'+file.split('.')[0]+'.jpg '
            with open(file_path) as fp:
                obj = json.load(fp)
            for i in range(len(obj['shapes'])):
                points = obj['shapes'][i]['points']
                x1 = points[0][0]
                y1 = points[0][1]
                x2 = points[1][0]
                y2 = points[1][1]
                xmin = x1 if x1 < x2 else x2
                xmax = x1 if x1 >= x2 else x2
                ymin = y1 if y1 < y2 else y2
                ymax = y1 if y1 >= y2 else y2
                buffer += str(int(xmin))+','+str(int(ymin))+','+str(int(xmax))+','+str(int(ymax))+','+'0 '
            print(buffer)
            buffer += '\n'
            writer.write(buffer)
        elif file.endswith('.xml'):
            buffer += '/home/boyu/temperory_annotation/' + file.split('.')[0] + '.jpg '
            root = ET.parse(file_path).getroot()
            for object in root.findall('object'):
                if 'person' == object.findtext('name') or 'people' == object.findtext('name'):
                    xmin = object.find('bndbox').findtext('xmin')
                    ymin = object.find('bndbox').findtext('ymin')
                    xmax = object.find('bndbox').findtext('xmax')
                    ymax = object.find('bndbox').findtext('ymax')
                    buffer += str(int(xmin)) + ',' + str(int(ymin)) + ',' + str(int(xmax)) + ',' + str(int(ymax)) + ',' + '0 '
                # elif 'notperson' == object.findtext('name') or 'notpeople' == object.findtext('name'):
                #     xmin = object.find('bndbox').findtext('xmin')
                #     ymin = object.find('bndbox').findtext('ymin')
                #     xmax = object.find('bndbox').findtext('xmax')
                #     ymax = object.find('bndbox').findtext('ymax')
                #     buffer += str(int(xmin)) + ',' + str(int(ymin)) + ',' + str(int(xmax)) + ',' + str(int(ymax)) + ',' + '1 '
            print(buffer)
            buffer += '\n'
            writer.writelines(buffer)
        else:
            continue

