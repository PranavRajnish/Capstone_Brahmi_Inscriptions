import numpy as np
import cv2
import os

dataset_path = 'OCR_Dataset\RecognizerDataset_150_210'
images = []
class_ids = []
dirs = os.listdir(dataset_path)
no_of_classes = len(dirs)

for class_id in dirs:
    imageList = os.listdir(os.path.join(dataset_path, str(class_id)))
    for image_name in imageList:
        curImg = cv2.imread(os.path.join(dataset_path, str(class_id), str(image_name)))
        curImg = cv2.resize(curImg, (32,32))
        images.append(curImg)
        class_ids.append(class_id)
    print(class_id)
