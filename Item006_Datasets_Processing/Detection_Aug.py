# 数据集扩增

import cv2
import math
import numpy as np
import xml.etree.ElementTree as ET
import os


def rotate_image(src, angle, scale=1):
    w = src.shape[1]
    h = src.shape[0]
    # 角度变弧度
    rangle = np.deg2rad(angle)  # angle in radians
    # now calculate new image width and height
    nw = (abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)) * scale
    nh = (abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)) * scale
    # ask OpenCV for the rotation matrix
    rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale)
    # calculate the move from the old center to the new center combined
    # with the rotation
    rot_move = np.dot(rot_mat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))
    # the move only affects the translation, so update the translation
    # part of the transform
    rot_mat[0, 2] += rot_move[0]
    rot_mat[1, 2] += rot_move[1]
    dst = cv2.warpAffine(src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)
    # 仿射变换
    return dst

# 对应修改xml文件
def rotate_xml(src, xmin, ymin, xmax, ymax, angle, scale=1.):
    w = src.shape[1]
    h = src.shape[0]
    rangle = np.deg2rad(angle)  # angle in radians
    # now calculate new image width and height
    # 获取旋转后图像的长和宽
    nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
    nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
    # ask OpenCV for the rotation matrix
    rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
    # calculate the move from the old center to the new center combined
    # with the rotation
    rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5,0]))
    # the move only affects the translation, so update the translation
    # part of the transform
    rot_mat[0, 2] += rot_move[0]
    # rot_mat是最终的旋转矩阵
    rot_mat[1, 2] += rot_move[1]
    # 获取原始矩形的四个中点，然后将这四个点转换到旋转后的坐标系下
    point1 = np.dot(rot_mat, np.array([(xmin+xmax)/2, ymin, 1]))
    point2 = np.dot(rot_mat, np.array([xmax, (ymin+ymax)/2, 1]))
    point3 = np.dot(rot_mat, np.array([(xmin+xmax)/2, ymax, 1]))
    point4 = np.dot(rot_mat, np.array([xmin, (ymin+ymax)/2, 1]))
    concat = np.vstack((point1, point2, point3, point4))   # 合并np.array
    # 改变array类型
    concat = concat.astype(np.int32)
    # rx,ry,为新的外接框左上角坐标，rw为框宽度，rh为高度，新的xmax=rx+rw,新的ymax=ry+rh
    rx, ry, rw, rh = cv2.boundingRect(concat)
    return rx, ry, rw, rh

# 使图像旋转60,90,120,150,210,240,300度
imgpath = 'C:/dataset/1/'  #源图像路径
xmlpath = 'C:/dataset/2/'  #源图像所对应的xml文件路径
rotated_imgpath = 'C:/dataset/3/'
rotated_xmlpath = 'C:/dataset/4/'
for angle in (15, 30, 45, 60, 75, 90, 105, 120):
    for i in os.listdir(imgpath):
        a, b = os.path.splitext(i) # 分离出文件名a
        img = cv2.imread(imgpath + a + '.jpg')
        rotated_img = rotate_image(img,angle)
        cv2.imwrite(rotated_imgpath + a + '_'+ str(angle) +'d.jpg',rotated_img)
        print(str(i) + ' has been rotated for '+ str(angle)+'°')
        tree = ET.parse(xmlpath + a + '.xml')
        root = tree.getroot()
        for box in root.iter('bndbox'):
            xmin = float(box.find('xmin').text)
            ymin = float(box.find('ymin').text)
            xmax = float(box.find('xmax').text)
            ymax = float(box.find('ymax').text)
            x, y, w, h = rotate_xml(img, xmin, ymin, xmax, ymax, angle)
            # 可在该步骤测试新画的框位置是否正确
            # cv2.rectangle(rotated_img, (x, y), (x+w, y+h), [0, 0, 255], 2)
            # cv2.imshow('xmlbnd',rotated_img)
            # cv2.waitKey(200)
            box.find('xmin').text = str(x)
            box.find('ymin').text = str(y)
            box.find('xmax').text = str(x+w)
            box.find('ymax').text = str(y+h)
        tree.write(rotated_xmlpath + a + '_' + str(angle) +'d.xml')
        print(str(a) + '.xml has been rotated for ' + str(angle)+'°')