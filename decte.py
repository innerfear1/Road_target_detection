
import os
import time

from PIL import Image
folder_path = 'E:\\pycharm_project\\YOLOV7_RSR\\VOCdevkit\\VOC2007\\JPEGImages'
extensions = []
index=0


for filee in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filee)
    print('** Path: {}  **'.format(file_path), end="\r", flush=True)
    print(file_path)
    im = Image.open(file_path)
    rgb_im = im.convert('RGB')
    time.sleep(0.5)
