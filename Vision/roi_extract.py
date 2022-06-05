import cv2
import os
import matplotlib.pyplot as plt

h = w = 25  # 提取区域的长宽
img_path = "./home/pi/Documents/CuBiC/Vision/picture"
'''--------------------------------------------------------------------------------'''
x1, y1 = 1000, 1000
x2, y2 = 2000, 2000
x3, y3 = 1, 2
x4, y4 = 3, 4
x5, y5 = 5, 6  # 一个面中心色块
x6, y6 = 5, 6
x7, y7 = 5, 6
x8, y8 = 5, 6
x9, y9 = 5, 6
'''--------------------------------------------------------------------------------
包含两个面'''
x10, y10 = 5, 6
x11, y11 = 5, 6
x12, y12 = 5, 6
x13, y13 = 5, 6
x14, y14 = 5, 6  # 一个面中心色块
x15, y15 = 5, 6
x16, y16 = 5, 6
x17, y17 = 5, 6
x18, y18 = 5, 6

x19, y19 = 5, 6
x20, y20 = 5, 6
x21, y21 = 5, 6
x22, y22 = 5, 6
x23, y23 = 5, 6  # 一个面中心色块
x24, y24 = 5, 6
x25, y25 = 5, 6
x26, y26 = 5, 6
x27, y27 = 5, 6
'''-------------------------------------------------------------------------------
包含两个面'''
x28, y28 = 5, 6
x29, y29 = 5, 6
x30, y30 = 5, 6
x31, y31 = 5, 6
x32, y32 = 5, 6  # 一个面中心色块
x33, y33 = 5, 6
x34, y34 = 5, 6
x35, y35 = 5, 6
x36, y36 = 5, 6

x37, y37 = 5, 6
x38, y38 = 5, 6
x39, y39 = 5, 6
x40, y40 = 5, 6
x41, y41 = 5, 6  # 一个面中心色块
x42, y42 = 5, 6
x43, y43 = 5, 6
x44, y44 = 5, 6
x45, y45 = 5, 6
'''--------------------------------------------------------------------------------'''
x46, y46 = 5, 6
x47, y47 = 5, 6
x48, y48 = 5, 6
x49, y49 = 5, 6
x50, y50 = 5, 6  # 一个面中心色块
x51, y51 = 5, 6
x52, y52 = 5, 6
x53, y53 = 5, 6
x54, y54 = 5, 6
'''---------------------------------------------------------------------------------'''
X = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25,
     x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46, x47, x48,
     x49, x50, x51, x52, x53, x54]  # 存储左上角坐标x值的矩阵
Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20, y21, y22, y23, y24, y25,
     y26, y27, y28, y29, y30, y31, y32, y33, y34, y35, y36, y37, y38, y39, y40, y41, y42, y43, y44, y45, y46, y47, y48,
     y49, y50, y51, y52, y53, y54]  # 存储左上角坐标y值的矩阵


def cv2_show(name, a) -> None:
    cv2.namedWindow(name, 0)
    cv2.imshow(name, a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def roi_extract(img_path) -> list:
    roi_s = []  # 用于储存提取的roi
    for file in os.listdir(img_path):
        file_path = os.path.join(img_path, file)
        img = cv2.imread(file_path)
        for x, y in zip(X, Y):
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
            plt.subplot(3, 6, i)
            plt.imshow(img)
            i += 1
        plt.show()
