# -*- coding:UTF-8 -*-

import cv2
import numpy as np


def calc():
    vid_cap = cv2.VideoCapture('calc_time.py.mp4')
    count = 0
    success = True
    while success:
        success, frame = vid_cap.read()  # 读取视频中的每一帧图像
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 将帧图像格式转换到HSV格式
        lower_blue = np.array([110, 50, 50])  # 设置蓝色阈值下限
        upper_blue = np.array([130, 255, 255])  # 设置蓝色阈值上限
        mask = cv2.inRange(hsv, lower_blue, upper_blue)  # 根据阈值构建掩模

        res = cv2.bitwise_and(frame, frame, mask=mask)  # 对原图像和掩模进行位运算

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        if cv2.waitKey(10) == 27:
            break
        count += 1
    cv2.destroyAllWindows()


def image_test():
    img = cv2.imread("img/frame293.jpg", cv2.IMREAD_COLOR)
    cv2.imshow("imread_color", img)

    img1 = cv2.imread("img/frame256.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("imread_grayscale", img1)
    cv2.imwrite("copy_gray_file.png", img1)

    cv2.namedWindow("window_normal", cv2.WINDOW_NORMAL)  # 自定义窗口大小， 默认为WINDOW_AUTOSIZE
    img2 = cv2.imread("7.jpg", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("window_normal", img2)

    # 官方建议： 64位机器上使用 cv2.waitKey(0) & 0xff
    b = cv2.waitKey(0) & 0xff  # 敲击任意按键，程序继续运行， 返回键盘码
    print(b)
    cv2.destroyAllWindows()


def video_camera_test():
    cap = cv2.VideoCapture(0)  # 调用摄像头
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame', gray)
        # 等1毫秒，判断是否按了 “q”键
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def video_file_test():
    cap = cv2.VideoCapture("calc_time.py.mp4")
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT), cap.get(cv2.CAP_PROP_FRAME_COUNT))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放资源
    cap.release()
    cv2.destroyAllWindows()


def save_camera_file():
    cap = cv2.VideoCapture("10.mp4")
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('102.mp4', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 0)
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def img_append_sth():
    img = cv2.imread("start.png", cv2.IMREAD_COLOR)
    height, width = img.shape[0], img.shape[1]
    cv2.rectangle(img, (0, height - 30), (width, height), (0, 0, 0), 30)

    cv2.imshow("imread_color", img)

    # 官方建议： 64位机器上使用 cv2.waitKey(0) & 0xff
    b = cv2.waitKey(0) & 0xff  # 敲击任意按键，程序继续运行， 返回键盘码
    print(b)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # image_test()
    # save_camera_file()
    img_append_sth()
    pass

