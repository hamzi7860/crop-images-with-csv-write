# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:44:19 2020

@author: Windows7
"""


import csv
from io import BytesIO
import requests
from PIL import Image

def write_in_csv(img_list):
    j = 0
    full_labels = open('D:/BS-EE/CONVSYS_Internship/New_Interns/Hadi/01/July 6, 2020/labels.csv','r')
    new_csv = open('D:/BS-EE/CONVSYS_Internship/New_Interns/Hadi/01/July 6, 2020/new_csv.csv','w')
    reader = csv.reader(full_labels)
    new_csv.write("Image"+","+"Sub-Cat"+","+"Sex"+","+"Color"+","+"Design/Pattern"+","+"Type"+","+"Material"+"Size/Shape"+"\n")
    for row in full_labels:
        if j<len(img_list):
            lines = row.split(',')
            new_csv.write(img_list[j] +','+lines[5]+','+lines[6]+','+lines[7]+','+lines[8]+','+lines[9]+','+lines[10]+','+lines[11]+'\n')
            j+=1

# open file to read
with open("D:/BS-EE/CONVSYS_Internship/New_Interns/Hadi/01/July 6, 2020/labels.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
   
    
    # iterate on all lines
    i = 0
    img_list = []
    for line in csvfile:
        splitted_line = line.split(',')
        # check if we have an image URL
        if splitted_line[0] != '' and splitted_line[0] != "\n":
            #response = requests.get(splitted_line[1])
            img = Image.open(r"D:/BS-EE/CONVSYS_Internship/New_Interns/Hadi/01/July 6, 2020/jpegs/"+splitted_line[0])

            #im.crop(box) ⇒ 4-tuple defining the left, upper, right, and lower pixel coordinate
            left_x = int(splitted_line[1])
            top_y = int(splitted_line[2])
            right_x = int(splitted_line[3])
            bottom_y = int(splitted_line[4])
            crop = img.crop((left_x, top_y, right_x, bottom_y))
            new_img = crop.resize((256, 256))
            """ 
            # preview new images
            imgplot = plt.imshow(new_img)
            plt.show()
            """
            img_name = str(i) + ".jpg"
            new_img.save(img_name)
            img_list.append(img_name)
            print("Image saved for {0}".format(splitted_line[0]))
            i += 1
            
        else:
            print("No result for {0}".format(splitted_line[0]))
            
        write_in_csv(img_list)
