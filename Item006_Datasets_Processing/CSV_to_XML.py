# encoding: utf-8
import csv
import cv2

newRows = []
with open("E:/Steel bar Calculation/test/train_labels.csv", "r") as fr:
    rows = csv.reader(fr)
    aRow = []
    lastJpg = ''
    newJpg = ''
    count = 0
    for row in rows:
        newJpg = row[0]
        if newJpg != lastJpg:
            if aRow:
                newRows.append(aRow)
            aRow=row
        else:
            aRow.append(row[1])   
        lastJpg = row[0]
        count += 1
    newRows.append(aRow)            


def getXml(jpgDetail):
    context = "<annotation>\n"
    context += "\t<folder>JPGImage</folder>\n"
    context += "\t<filename>"+jpgDetail[0]+"</filename>\n"
    context += "\t<path>/MYPATH/JPGImage/"+jpgDetail[0]+"</path>\n"
    context += "\t<source>\n"
    context += "\t\t<database>Unknown</database>\n"
    context += "\t</source>\n"
    context += "\t<size>\n"
    path_img = "E:/Steel bar Calculation/test/train_dataset/"+jpgDetail[0]
    print("path_img", path_img)
    # 返回一个Image对象
    img = cv2.imread("E:/Steel bar Calculation/test/train_dataset/"+jpgDetail[0])
    print(img)
    sp = img.shape
    context += "\t\t<width>"+str(sp[1])+"</width>\n"
    context += "\t\t<height>"+str(sp[0])+"</height>\n"
    context += "\t\t<depth>"+str(sp[2])+"</depth>\n"
    context += "\t</size>\n"
    context += "\t<segmented>0</segmented>\n"
    for i in range(len(jpgDetail)):
        if not i or not jpgDetail[i]:
            continue
        context +="\t<object>\n"
        context +="\t\t<name>count</name>\n"
        context +="\t\t<pose>Unspecified</pose>\n"
        context +="\t\t<truncated>0</truncated>\n"
        context +="\t\t<difficult>0</difficult>\n"
        context +="\t\t<bndbox>\n"
        pic = jpgDetail[i].strip().split()
        context += "\t\t\t<xmin>"+pic[0]+"</xmin>\n"
        context += "\t\t\t<ymin>"+pic[1]+"</ymin>\n"
        context += "\t\t\t<xmax>"+pic[2]+"</xmax>\n"
        context += "\t\t\t<ymax>"+pic[3]+"</ymax>\n"
        context += "\t\t</bndbox>\n"
        context += "\t</object>\n"
    context += "</annotation>\n"
    return context

print("E:/Steel bar Calculation/test/"+newRows[1][0][:-3]+"xml")
print(newRows[1][0])
for i in range(1,len(newRows)):
    outputF = open("E:/Steel bar Calculation/test/xmls/"+newRows[i][0][:-3]+"xml", 'w+')
    outputF.write(getXml(newRows[i]))
    outputF.close()

for i in newRows:
    print(i)
