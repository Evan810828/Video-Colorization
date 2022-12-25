import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle


def color_slicing(image, skin, hair, background, w):
    """
    :param image:
    :param center: b, g, r ib range 0 ~ 255
    :param w: width
    :return:
    """
    skin0 = np.zeros([image.shape[0], image.shape[1]], np.uint8)
    hair0 = np.zeros([image.shape[0], image.shape[1]], np.uint8)
    background0 = np.zeros([image.shape[0], image.shape[1]], np.uint8)
    cloth0 = np.zeros([image.shape[0], image.shape[1]], np.uint8)
    h_b, h_g, h_r = hair
    s_b, s_g, s_r = skin
    b_b, b_g, b_r = background
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            a_b, a_g, a_r = image[x][y]
            if abs(h_b - a_b) < w / 2 and abs(h_g - a_g) < w / 2 and abs(h_r - a_r) < w / 2:
                hair0[x][y] = 255
            elif abs(s_b - a_b) < w / 2 and abs(s_g - a_g) < w / 2 and abs(s_r - a_r) < w / 2:
                skin0[x][y] = 255
            elif abs(b_b - a_b) < w / 2 and abs(b_g - a_g) < w / 2 and abs(b_r - a_r) < w / 2:
                background0[x][y] = 255
    cloth0 += (skin0 + hair0 + background0)
    cloth0 = np.zeros([image.shape[0], image.shape[1]], np.uint8) + 255 - cloth0
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    cloth0 = cv2.erode(cloth0, kernel1, iterations=1)
    hair0 = cv2.erode(hair0, kernel2, iterations=1)
    skin0 = cv2.erode(skin0, kernel2, iterations=1)
    background0 = cv2.erode(background0, kernel2, iterations=1)
    cloth0 = cv2.GaussianBlur(cloth0, (15, 15), 15)
    hair0 = cv2.GaussianBlur(hair0, (15, 15), 15)
    skin0 = cv2.GaussianBlur(skin0, (15, 15), 15)
    background0 = cv2.GaussianBlur(background0, (15, 15), 15)
    return skin0, hair0, cloth0, background0

def color_slicing2(image, data):
    """
    :param image:
    :param center: b, g, r ib range 0 ~ 255
    :param w: width
    :return:
    """
    key_value = list(data.keys())
    res = []
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    for i in key_value:
        temp = np.zeros([image.shape[0], image.shape[1]], np.uint8)
        for j in data[i]:
            temp[j[0]][j[1]] = 255
        temp = cv2.dilate(temp, kernel, iterations=1)
        temp = cv2.GaussianBlur(temp, (15, 15), 15)
        res.append(temp)
    return res


def dyeing(channel, reference):
    image = reference[0]
    for i in range(1, len(channel)):
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                a = channel[i][x][y] / 255
                image[x][y] = a*reference[i][x][y] + (1-a)*image[x][y]
    return image

image = cv2.imread('parsing_results\\parsing_results\\select_pics\\demo12.jpg')
image0 = cv2.imread('parsing_results\\parsing_results\\reference\\11_0.jpg')
image1 = cv2.imread('parsing_results\\parsing_results\\reference\\11_1.jpg')
image2 = cv2.imread('parsing_results\\parsing_results\\reference\\11_2.jpg')
image3 = cv2.imread('parsing_results\\parsing_results\\reference\\11_3.jpg')
image4 = cv2.imread('parsing_results\\parsing_results\\reference\\11_4.jpg')
image5 = cv2.imread('parsing_results\\parsing_results\\reference\\11_5.jpg')

with open("parsing_results\parsing_results\crop_pic_parsing\demo12.pkl", 'rb') as handle:
        data = pickle.load(handle)

channel = color_slicing2(image, data)
reference = [image0, image1, image2, image3, image4, image5]
res = dyeing(channel, reference)
cv2.imshow('res', res)
cv2.waitKey(0)
