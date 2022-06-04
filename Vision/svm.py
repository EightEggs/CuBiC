import numpy as np
import os
import joblib
import cv2
from roi_extract import roi_extract
# svm颜色识别(一张图片)

model_path = './svm_cube.model'
clf = joblib.load(model_path)  # 加载模型


def img2vector(img):  # 图片转向量
    img_arr = np.array(img)
    img_normlization = img_arr / 255
    img_arr2 = np.reshape(img_normlization, (1, -1))
    return img_arr2


def color_detect(img) -> list:  # 利用训练好的module进行颜色检测
    preResults = []  # 用来储存得到颜色的数组
    img_rois = roi_extract(img)
    for img_roi in img_rois:
        img2arr = img2vector(img_roi)
        preResult = clf.predict(img2arr)
        preResults.append(''.join(str(i) for i in list(preResult)))
    return preResults


if __name__ == '__main__':
    img_path = "./test"
    for file in os.listdir(img_path):
        filepath = os.path.join(img_path, file)
        img = cv2.imread(filepath)
        preResults = color_detect(img)
        print(preResults)
