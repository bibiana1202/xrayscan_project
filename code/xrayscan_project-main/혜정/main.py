import pickle

import pandas as pd
import numpy as np

import requests

from bs4 import BeautifulSoup
import os

#input
PATH_train_xml='/Applications/codeBox/xrayScan_project/data/train_xml/'

#output
PATH_xray='/Applications/codeBox/xrayScan_project/'
PATH_text='/Applications/codeBox/xrayScan_project/data/train_txt/'

# 라벨 설정
class_names = ['Aerosol','Alcohol','Awl','Axe','Bat','Battery',"Bullet"
,"Chisel","Electronic cigarettes","Electronic cigarettes(Liquid)","Firecracker"
,"Gun","GunParts","Hammer","HandCuffs","HDD","HDD_External","Knife","Laptop"
,"Lighter","Liquid","Match","MetalPipe","NailClippers","Plier","PrtableGas"
,"Saw","Scissors","Screwdriver","SmartPhone","SolidFuel","Spanner","SSD"
,"SupplymentaryBattery","TabletPC","Thinner","Throwing Knife","USB","ZippoOil"]

print(len(class_names))


import os

dir_path = 

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
