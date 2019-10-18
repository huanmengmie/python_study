# -*- coding:UTF-8 -*-
import math
import os

import cv2
import numpy as np


def video_to_image():
    """
    将视频转化为图片
    :return:
    """
    count = 0
    cap = cv2.VideoCapture("10.mp4")  # capturing the video from the given path
    frame_rate = cap.get(cv2.CAP_PROP_FPS)  # frame rate
    x = 1
    while cap.isOpened():
        frameId = cap.get(1)  # current frame number
        ret, frame = cap.read()
        if not ret:
            break
        if frameId % math.floor(frame_rate / 10) == 0:
            filename = os.path.join(os.path.dirname(__file__), "img", "frame%d.jpg" % count)
            count += 1
            cv2.imwrite(filename, frame)
    cap.release()
    print("Done!")


def check_color():
    """
    判断是否有指定的颜色
    :return:
    """
    src = cv2.imread("start.png")
    cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("input", src)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([0, 0, 0])
    high_hsv = np.array([180, 255, 46])
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
    print("没有找到" if np.all(mask == 0) else "找到了")
    cv2.imshow("test", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def find_difference():
    img1 = cv2.imread("img/")


if __name__ == '__main__':
    # video_to_image()
    check_color()
    pass
