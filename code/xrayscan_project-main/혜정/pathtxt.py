from pathlib import WindowsPath
import os

#input
PATH_train_xml='/Applications/codeBox/xrayScan_project/data/train_xml/'
# 이후 이미지 데이터셋을 저장할 경로 지정
PATH_images='/Applications/codeBox/xrayScan_project/darknet/data/images/'
PATH_data='/Applications/codeBox/xrayScan_project/darknet/data/'

#output
PATH_xray='/Applications/codeBox/xrayScan_project/'
PATH_text='/Applications/codeBox/xrayScan_project/data/txt/'


# train.txt 생성
# w 모드로 text 파일을 생성
f = open('/content/darknet/data/train.txt', 'w')
for img in os.listdir('/content/train'):
    if img[-3:]=='jpg':
        # 문자 입력
        f.write(path+img+"\n")
f.close()


# test.txt 생성
# w 모드로 text 파일을 생성
f = open('/content/darknet/data/test.txt', 'w')
for img in os.listdir('/content/test'):
    if img[-3:]=='jpg':
        # 문자 입력
        f.write(path+img+"\n")
f.close()



"""# valid.txt 생성
# w 모드로 text 파일을 생성
f = open('/content/darknet/data/valid.txt', 'w')
for img in os.listdir('/content/valid'):
    if img[-3:]=='jpg':
        # 문자 입력
        f.write(path+img+"\n")
f.close()
"""

# mask_data.data에 기록

t.write("train = data/train.txt\n")
t.write("valid = data/valid.txt\n")
t.write("test = data/test.txt\n")