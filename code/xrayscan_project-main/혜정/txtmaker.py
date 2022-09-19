import pickle

import pandas as pd
import numpy as np

import requests

from bs4 import BeautifulSoup
import os




#input
PATH_data_xml='/Applications/codeBox/xrayScan_project/data/data_xml/'

#output
PATH_xray='/Applications/codeBox/xrayScan_project/'
PATH_text='/Applications/codeBox/xrayScan_project/data/data_txt/'

# 라벨 설정
class_names = ['Aerosol','Alcohol','Awl','Axe','Bat','Battery',"Bullet"
,"Chisel","Electronic cigarettes","Electronic cigarettes(Liquid)","Firecracker"
,"Gun","GunParts","Hammer","HandCuffs","HDD","HDD_External","Knife","Laptop"
,"Lighter","Liquid","Match","MetalPipe","NailClippers","Plier","PrtableGas"
,"Saw","Scissors","Screwdriver","SmartPhone","SolidFuel","Spanner","SSD"
,"SupplymentaryBattery","TabletPC","Thinner","Throwing Knife","USB","ZippoOil"]

print(len(class_names))



from pathlib import WindowsPath
import os

train_xml_list = os.listdir(PATH_data_xml)

## Train의 xml 파일 137708 이름 list
filename_TX = [file for file in train_xml_list if file.endswith('.xml')] 
print(len(filename_TX))

from xml.etree.ElementTree import parse
dic_xml = {
      'size_w':[],
      'size_h':[],
      'filename':[],
      'name':[],
      'x':[],
      'y':[],
      'width':[],
      'height':[]
}
for i,filename in enumerate(filename_TX):
  print(i,filename)
  dict_xml = {
      'name':[],
      'x':[],
      'y':[],
      'width':[],
      'height':[]
  }

  tree = parse(PATH_data_xml+filename)
  root = tree.getroot()

  object_xml = root.findall("object")

  name = [x.findtext("name") for x in object_xml]

  bndbox = [x.find("bndbox") for x in object_xml]

  
  for j in range(len(bndbox)):
    name_index = class_names.index(name[j])
    dict_xml['name'].append(name_index)
    
    size_width =1920
    size_height =1080

    size_width = float(size_width/4)
    size_height = float(size_height/4)
    
    xmin=float(bndbox[j].findtext('xmin'))
    xmax=float(bndbox[j].findtext('xmax'))
    ymin=float(bndbox[j].findtext('ymin'))
    ymax=float(bndbox[j].findtext('ymax'))
    
    width= xmax - xmin
    height= ymax - ymin
    x= xmin + width/2
    y = ymin + height /2

    width= width/4
    height=height/4
    x = x/4
    y= y/4
    
    size_height = size_height + (480-270)
    y= y+ (480-270)/2
    
    # 480x480 정규화
    x = x / 480
    y = y /480
    width = width / 480
    height = height / 480
    
    
    
    
    
    # dict_append 하기
    dict_xml['x'].append(x)
    dict_xml['y'].append(y)
    dict_xml['width'].append(width)
    dict_xml['height'].append(height)
    
    
    
    
    
    #dic append 하기
    dic_xml['size_w'].append(size_width)
    dic_xml['size_h'].append(size_height)
    dic_xml['filename'].append(filename)
    dic_xml['name'].append(name_index)
    dic_xml['x'].append(x)
    dic_xml['y'].append(y)
    dic_xml['width'].append(width)
    dic_xml['height'].append(height)


    
  title = filename.split('.xml')[0]
  df_text = pd.DataFrame(dict_xml)
  df_text.to_csv(PATH_text+title+'.txt', sep = ' ',index = False,header=False)

df_data = pd.DataFrame(dic_xml)
df_data.to_csv(PATH_xray+'df_data_480.csv')
df_data.to_pickle(PATH_xray+'df_data_480.pickle')


