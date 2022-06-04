import cv2
import os
import matplotlib.pyplot as plt
# 切割出要识别的区域

h = w = 25  # 提取区域的长宽
# 最多16个色块的坐标
x1, y1 = 1000, 1000
x2, y2 = 2000, 2000
x3, y3 = 1, 2
x4, y4 = 3, 4
x5, y5 = 5, 6
x6, y6 = 5, 6
x7, y7 = 5, 6
x8, y8 = 5, 6
x9, y9 = 5, 6
x10, y10 = 5, 6
x11, y11 = 5, 6
x12, y12 = 5, 6
x13, y13 = 5, 6
x14, y14 = 5, 6
x15, y15 = 5, 6
x16, y16 = 5, 6
X = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16]  # 存储左上角坐标x值的矩阵
Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16]  # 存储左上角坐标y值的矩阵


def cv2_show(name, a) -> None:
    cv2.namedWindow(name, 0)
    cv2.imshow(name, a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def roi_extract(img) -> list:
    roi_s = []  # 用于储存提取的roi
    for x, y in X, Y:
        if x != 0 and y != 0:
            roi = img[y:y+h, x:x+w]
            roi_s.append(roi)
    return roi_s


if __name__ == '__main__':
    img_path = "./test"
    for file in os.listdir(img_path):
        filepath = os.path.join(img_path, file)
        img = cv2.imread(filepath)
        roi_s = roi_extract(img)
        i = 1
        for img_roi in roi_s:
            roi = cv2.cvtColor(img_roi, cv2.COLOR_BGR2RGB)
            plt.subplot(2, 3, i)
            plt.imshow(img)
            i += 1
        plt.show()
