# Author :Jungang_An
# Coding :utf - 8 -*-
# Time : 2020/4/2 16:15

import os
import os.path
import xml.etree.cElementTree as ET
import cv2
def draw(image_path, saved_path):
    '''
    :param image_path: 输入的图片和xml同一个文件夹路径
    :param saved_path: 输出画框后图片的文件夹的路径
    :return:画框数据集的结果
    '''
    src_path = image_path
    for file in os.listdir(src_path):
        print(file)
        file_name, suffix = os.path.splitext(file)
        if suffix == '.xml':
            # print(file)
            xml_path = os.path.join(src_path, file)
            image_path = os.path.join(src_path, file_name+'.jpg')
            img = cv2.imread(image_path)
            tree = ET.parse(xml_path)
            root = tree.getroot()
            for obj in root.iter('object'):
                name = obj.find('name').text
                xml_box = obj.find('bndbox')
                x1 = int(xml_box.find('xmin').text)
                x2 = int(xml_box.find('xmax').text)
                y1 = int(xml_box.find('ymin').text)
                y2 = int(xml_box.find('ymax').text)
                # bbox画框为蓝色
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), thickness=2)
                # 标签字体为绿色
                cv2.putText(img, name, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), thickness=2)
            cv2.imwrite(os.path.join(saved_path, file_name+'.jpg'), img)


if __name__ == '__main__':
    image_path = ("D:/code/Dataset analysis/RBC detection/result/")
    saved_path = ("D:/code/Dataset analysis/RBC detection/result/map/")
    draw(image_path, saved_path)
