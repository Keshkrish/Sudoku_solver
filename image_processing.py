import cv2
import numpy as np


def diff(a):
    return a[0]-a[1]

def change_color_and_get_perspective(image,blur=False):
    img=image.copy()


    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV, 39, 10)

    contours, heirarchies = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxarea = 0
    cnt = contours[0]
    for i in contours:
        if cv2.contourArea(i) > maxarea:
            cnt = i
            maxarea = cv2.contourArea(i)

    top_left = cnt[0][0]
    bottom_right = cnt[0][0]

    min_sum = max_sum = sum(cnt[0][0])
    min_dif = max_dif = diff(cnt[0][0])
    bottom_left = top_right = cnt[0][0]
    for i in cnt:
        if sum(i[0]) < min_sum:
            min_sum = sum(i[0])
            top_left = i[0]
        if sum(i[0]) > max_sum:
            max_sum = sum(i[0])
            bottom_right = i[0]
        if diff(i[0]) < min_dif:
            min_dif = diff(i[0])
            bottom_left = i[0]
        if diff(i[0]) > max_dif:
            max_dif = diff(i[0])
            top_right = i[0]

    pt1 = np.float32([top_left, top_right, bottom_right, bottom_left])
    pt2 = np.float32([[0, 0], [756, 0], [756, 756], [0, 756]])
    matrix = cv2.getPerspectiveTransform(pt1, pt2)
    result = cv2.warpPerspective(img, matrix, (756, 756))
    if blur:
        result=cv2.GaussianBlur(result,(5,5),0)
    return result


def get_digits(img):
    digits=[]
    for i in range(9):
        for j in range(9):
            a=img[i*84:i*84+84,j*84:j*84+84]
            digits.append(a)


    return digits

